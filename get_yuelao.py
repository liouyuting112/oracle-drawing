import urllib.request
import json

def get_gist_json(gist_url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(gist_url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            # The raw link is in the page
            import re
            match = re.search(r'href="(/ryantm/1c9fba3bef1225230531a2d76cacd716/raw/[^"]+\.json)"', html)
            if match:
                raw_url = "https://gist.github.com" + match.group(1)
                print(f"RAW_URL: {raw_url}")
                req_raw = urllib.request.Request(raw_url, headers=headers)
                with urllib.request.urlopen(req_raw) as resp_raw:
                    return resp_raw.read().decode('utf-8')
    except Exception as e:
        print(f"Error: {e}")
    return None

data = get_gist_json("https://gist.github.com/ryantm/1c9fba3bef1225230531a2d76cacd716")
if data:
    with open("yuelao_data.json", "w", encoding="utf-8") as f:
        f.write(data)
    print("SUCCESS")
else:
    print("FAILED")
