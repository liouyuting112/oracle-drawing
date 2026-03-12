import json
import os

files = [
    'tarot_major.json',
    'tarot_wands.json',
    'tarot_cups.json',
    'tarot_swords.json',
    'tarot_pentacles.json'
]
DATA_DIR = r"c:\Users\yyutingliu\Downloads\抽籤\data"
merged = []

for file in files:
    path = os.path.join(DATA_DIR, file)
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        merged.extend(data)

final_path = os.path.join(DATA_DIR, 'tarot.json')
with open(final_path, 'w', encoding='utf-8') as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

print(f"Merge complete: {len(merged)} tarot cards written to {final_path}")
