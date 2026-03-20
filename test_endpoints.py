import requests
import json

API_KEY = "AIzaSyBZS2s6oxGMs_sLvgnYTS5spP4QyYvzS_E"
endpoints = [
    f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={API_KEY}",
    f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}",
    f"https://generativelanguage.googleapis.com/v1/models?key={API_KEY}",
    f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
]

print("Testing Endpoints:")
for url in endpoints:
    try:
        response = requests.get(url) if "models?" in url else requests.post(url, json={"contents": [{"parts": [{"text": "hi"}]}]})
        print(f"URL: {url.split('?')[0]}")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")
