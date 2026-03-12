import json
import os

files = ['gy1.json', 'gy2.json', 'gy3.json', 'gy4.json']
DATA_DIR = r"c:\Users\yyutingliu\Downloads\抽籤\data"
merged = []

for file in files:
    path = os.path.join(DATA_DIR, file)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        merged.extend(data)

final_path = os.path.join(DATA_DIR, 'guanyin100.json')
with open(final_path, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"Merge complete: {len(merged)} items written to {final_path}")
