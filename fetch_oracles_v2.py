import urllib.request
import re
import json

def fetch_url(url, encoding='utf-8'):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return response.read().decode(encoding, errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def scrape_guanyin():
    url = "http://www.chance.org.tw/%E7%B1%A4%E8%A9%A9%E9%9B%86/%E8%A7%80%E9%9F%B3%E4%B8%80%E7%99%BE%E7%B1%A4/%E7%B1%A4%E8%A9%A9%E7%B6%B2%E2%80%A7%E8%A7%80%E9%9F%B3%E4%B8%80%E7%99%BE%E7%B1%A4.htm"
    # Chance.org.tw uses Big5 usually
    html = fetch_url(url, 'big5')
    if not html: return []
    
    # Pattern to find numbers and brief info
    # Example: <a href="001.htm"> 第一籤 上上 </a> ...
    pattern = re.compile(r'第(\d+)籤\s+([\u4e00-\u9fa5]{2})')
    matches = pattern.findall(html)
    
    # Since scraping 100 subpages is slow, I'll attempt a few sample ones 
    # to show the user and then synthesize the rest or provide a link.
    # But for now, let's just get the list.
    return matches

def fetch_yuelao():
    # Attempting to get the raw gist content
    # The gist ID is 1c9fba3bef1225230531a2d76cacd716
    # Looking for a raw link in the gist page
    gist_url = "https://gist.github.com/ryantm/1c9fba3bef1225230531a2d76cacd716"
    html = fetch_url(gist_url)
    if not html: return None
    
    # Look for the raw link to the JSON file
    # Example: /ryantm/1c9fba3bef1225230531a2d76cacd716/raw/something/....json
    match = re.search(r'href="(/ryantm/1c9fba3bef1225230531a2d76cacd716/raw/[^"]+\.json)"', html)
    if match:
        raw_url = "https://gist.github.com" + match.group(1)
        print(f"Found raw URL: {raw_url}")
        content = fetch_url(raw_url)
        return json.loads(content) if content else None
    return None

def main():
    print("Testing Guanyin scrape...")
    gy = scrape_guanyin()
    print(f"Found {len(gy)} Guanyin oracles.")
    
    print("\nTesting Yue Lao fetch...")
    yl = fetch_yuelao()
    if yl:
        print(f"Found Yue Lao data! Keys: {yl[0].keys() if isinstance(yl, list) else yl.keys()}")
    else:
        print("Failed to fetch Yue Lao data.")

if __name__ == "__main__":
    main()
