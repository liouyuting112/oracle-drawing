import json
import os

def count_oracles():
    total = 0
    data_dir = r"C:\Users\yyutingliu\Downloads\抽籤\data"
    tarot_prefixes = ["tarot", "gy", "mz"] # Excluding fragments or tarot
    
    # Let's see if gy1, mz1 etc. are actually oracles
    oracle_files = []
    for f in os.listdir(data_dir):
        if not f.endswith(".json"):
            continue
        if any(f.startswith(p) for p in ["tarot"]):
            continue
        oracle_files.append(f)
        
    for f in oracle_files:
        f_path = os.path.join(data_dir, f)
        try:
            with open(f_path, "r", encoding="utf-8") as file:
                items = json.load(file)
                count = len(items) if isinstance(items, list) else len(items.keys())
                total += count
                print(f"{f}: {count}")
        except Exception as e:
            print(f"Error reading {f}: {e}")
            
    print(f"\nTotal oracle sticks: {total}")

if __name__ == "__main__":
    count_oracles()
