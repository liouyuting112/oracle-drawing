import requests
import json

url = "https://spring-mountain-810dmazu-ai-seal.love7053150.workers.dev/"
payload = {
    "model": "qwen3-coder:30b", 
    "prompt": "你好，請自我介紹。", 
    "stream": False
}
headers = {"Content-Type": "application/json"}

print(f"📡 正在發送請求至 Cloudflare Worker: {url}...")
try:
    response = requests.post(url, json=payload, headers=headers, timeout=30)
    print(f"✅ 狀態碼: {response.status_code}")
    if response.status_code == 200:
        print("📝 回傳內容擷取:")
        print(response.text[:500])
    else:
        print(f"❌ 錯誤訊息: {response.text}")
except Exception as e:
    print(f"💥 發生異常: {e}")
