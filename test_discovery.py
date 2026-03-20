import requests
import json

API_KEY = "AIzaSyBZS2s6oxGMs_sLvgnYTS5spP4QyYvzS_E"
models_to_test = [
    "gemini-3.1-flash",
    "gemini-3.1-pro",
    "gemini-2.0-flash",
    "gemini-2.0-pro",
    "gemini-1.5-flash",
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro",
    "gemini-pro"
]

results = {}

for model in models_to_test:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={API_KEY}"
    payload = {"contents": [{"parts": [{"text": "hi"}]}]}
    try:
        response = requests.post(url, json=payload, timeout=5)
        results[model] = response.status_code
        if response.status_code == 200:
             print(f"[SUCCESS] {model} is working!")
             break
        else:
             print(f"[FAIL] {model}: {response.status_code}")
    except Exception as e:
        results[model] = str(e)

print("\nFinal Results:")
print(json.dumps(results, indent=2))
