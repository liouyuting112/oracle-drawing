import os
import json
import requests
import uvicorn
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Configuration ---
GEMINI_API_KEY = "AIzaSyBZS2s6oxGMs_sLvgnYTS5spP4QyYvzS_E"
MODEL_NAME = "gemini-1.5-flash"
GENERATE_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={GEMINI_API_KEY}"
MASTER_DB_PATH = "master_db.json"

# --- Initialization ---
app = FastAPI(title="Digital Oracle Master API")
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Master DB
with open(MASTER_DB_PATH, 'r', encoding='utf-8') as f:
    master_db = json.load(f)

# --- Models ---
class PredictRequest(BaseModel):
    system: str  # 'eastern' or 'western'
    type: Optional[str] = None # e.g., 'mazu60'
    id: Optional[int] = None   # Oracle ID
    cards: Optional[list] = None # List of tarot card names/objs
    question: str = ""
    category: str = "其他"

# --- Logic ---
def is_complex_question(question: str) -> bool:
    """
    Determine if the question needs AI or just static interpretation.
    """
    if not question or len(question.strip()) < 5:
        return False
    # Simple check for specific intent
    keywords = ["機率", "時間", "買房", "結婚", "分手", "轉職", "建議", "如何", "為什麼", "何時"]
    if any(k in question for k in keywords):
        return True
    return len(question) > 10

def get_gemini_response(prompt: str):
    try:
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        res = requests.post(GENERATE_URL, json=payload, timeout=30)
        if res.status_code == 200:
            data = res.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]
        return f"Gemini API Error: {res.status_code} - {res.text}"
    except Exception as e:
        return f"Connection to Gemini failed: {str(e)}"

# --- API Endpoints ---

@app.get("/")
async def root():
    return {"status": "online", "message": "Digital Oracle Master is ready."}

@app.post("/api/predict")
@limiter.limit("5/minute") # Only 5 requests per minute per IP to avoid abuse
async def predict(req: PredictRequest, request: Request):
    # 1. Basic Data Retrieval
    oracle_data = None
    if req.system == 'eastern':
        type_data = master_db["oracles"].get(req.type, [])
        oracle_data = next((i for i in type_data if i['id'] == req.id), None)
        if not oracle_data:
            raise HTTPException(status_code=404, detail="Oracle not found")
    else:
        # Tarot logic (simplified for this example, fetching meanings from DB)
        oracle_data = {"name": "Tarot Multiple", "cards": req.cards}

    # 2. Decision: AI or Static?
    use_ai = is_complex_question(req.question)
    
    if not use_ai:
        # Return static interpretation from DB
        # If the DB has specific category interpretation, use it
        return {
            "mode": "static",
            "data": oracle_data,
            "interpretation": oracle_data.get("interpretation", "順應天理，隨遇而安。")
        }
    else:
        # Prepare Prompt for H200
        if req.system == 'eastern':
            prompt = f"你是命理大師。使用者抽取了『{req.type}』第{req.id}籤。\n"
            prompt += f"籤文：{oracle_data.get('poem', '')}\n"
            prompt += f"典故：{oracle_data.get('story', '')}\n"
            prompt += f"使用者提問：{req.question}\n"
            prompt += "請根據籤意，深入分析使用者的問題，給出具體且溫暖的建議。用繁體中文回答。"
        else:
            prompt = f"你是塔羅大師。使用者抽取的牌陣如下：\n"
            for c in req.cards:
                prompt += f"- {c['pos']}: {c['name']} ({c['dir']})\n"
            prompt += f"使用者提問：{req.question}\n"
            prompt += "請根據牌面能量與關聯性，深度解答使用者的疑惑。用繁體中文回答。"
        
        ai_response = get_gemini_response(prompt)
        return {
            "mode": "ai",
            "data": oracle_data,
            "interpretation": ai_response
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
