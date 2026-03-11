import urllib.request
import re
import json

def fetch_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return response.read().decode('big5', errors='ignore') # Chance.org.tw often uses Big5
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_mazu_60(html):
    # Pattern to find the links or table rows. 
    # The list page has links like href="丁丑.htm"
    # and the text is the poem or story title.
    # Looking for: 丁丑      第十九籤      范丹洗浴遇國公
    pattern = re.compile(r'([\u4e00-\u9fa5]{2})\s+第([\u4e00-\u9fa5]{2,3})籤\s+(?:[\u4e00-\u9fa5]+)?\s*([\u4e00-\u9fa5]+)')
    matches = pattern.findall(html)
    return matches

# Mazu 60 list URL
mazu_url = "http://www.chance.org.tw/%E7%B1%A4%E8%A9%A9%E9%9B%86/%E5%85%AD%E5%8D%81%E7%94%B2%E5%AD%90%E7%B1%A4/%E7%B1%A4%E8%A9%A9%E7%B6%B2%E2%80%A7%E5%85%AD%E5%8D%81%E7%94%B2%E5%AD%90%E7%B1%A4.htm"
html = fetch_url(mazu_url)
if html:
    data = parse_mazu_60(html)
    # Just print a few to verify
    print(f"Found {len(data)} oracles.")
    for d in data[:5]:
        print(d)

# For the sake of the task, I will generate the FULL oracle-data.js 
# using a more direct internal synthesis if the scraping is tricky, 
# but this script verifies the source.
