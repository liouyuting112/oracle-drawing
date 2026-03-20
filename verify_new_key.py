import requests
import json

NEW_KEY = "AIzaSyAP8O5sqikGJ9p3Gndhc9XVRco8H1wTJUI"
models = ["gemini-3.1-flash", "gemini-1.5-flash", "gemini-1.5-flash-latest", "gemini-pro"]

print(f"Testing New Key: {NEW_KEY}")
for m in models:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={NEW_KEY}"
    try:
        r = requests.post(url, json={"contents": [{"parts": [{"text": "hi"}]}]}, timeout=10)
        print(f"{m}: Status {r.status_code}")
        if r.status_code != 200:
            print(f"   Error: {r.text[:200]}")
    except Exception as e:
        print(f"{m}: Error {e}")
