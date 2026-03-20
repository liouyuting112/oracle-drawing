import requests
import json

API_KEY = "AIzaSyBZS2s6oxGMs_sLvgnYTS5spP4QyYvzS_E"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

try:
    response = requests.get(url)
    data = response.json()
    if "models" in data:
        print("Available models:")
        for model in data["models"]:
            print(f"- {model['name']}")
    else:
        print("Could not retrieve models list.")
        print(json.dumps(data, indent=2))
except Exception as e:
    print(f"Error: {e}")
