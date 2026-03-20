import requests
import json

API_KEY = "AIzaSyBZS2s6oxGMs_sLvgnYTS5spP4QyYvzS_E"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

payload = {
    "contents": [{"parts": [{"text": "Hello, are you working?"}]}]
}

try:
    response = requests.post(url, json=payload)
    print(f"Status Code: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {e}")
