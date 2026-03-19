import os
import json

DATA_DIR = r"C:\Users\yyutingliu\Downloads\研究地端模型\抽籤\data"
OUTPUT_FILE = r"C:\Users\yyutingliu\Downloads\研究地端模型\抽籤\master_db.json"

ORACLE_TYPES = {
    'mazu60': '媽祖六十甲子籤',
    'guanyin100': '觀音一百籤',
    'guandi100': '雷雨師一百籤 (關帝/城隍)',
    'tudigong28': '土地公廿八籤 (烘爐地)',
    'yuelao': '月老靈籤 (100籤)',
    'zhuge384': '諸葛神算 (384籤)',
    'sevenkings60': '東港鎮海宮七王爺靈籤',
    'baosheng60': '保生大帝六十籤',
    'qingshui50': '清水祖師五十籤',
    'luzu100': '呂祖靈籤一百籤',
    'luzu60': '呂仙祖六十籤 (指南宮)',
    'zhusheng30': '註生娘娘三十籤',
    'beidi51': '北帝靈籤 (五十一籤)',
    'fourface30': '四面佛三十籤',
    'caishin100': '五路財神一百籤',
    'beidi100': '北帝一百籤 (罕見版)',
    'guanyin28': '觀音廿八籤 (小型)',
    'guanyin24': '觀音廿四籤 (精簡)',
    'zodiac28': '二十八星宿籤',
    'pienchu100': '扁鵲神醫藥籤 (100籤)',
    'yaoqian50': '藥籤 (五十籤)',
    'yaoqian200': '藥籤 (二百籤)',
    'lukang100': '鹿港天后宮一百籤',
    'penghu100': '澎湖天后宮一百籤',
    'zhuge64': '諸葛孔明六十四籤 (金錢卦)',
    'zhuge32': '諸葛孔明三十二籤 (金錢卦)',
    'tarot': '塔羅牌 (78張)'
}

def consolidate():
    master_db = {
        "oracles": {},
        "tarot": []
    }
    
    total_count = 0
    
    for filename in os.listdir(DATA_DIR):
        if not filename.endswith(".json"):
            continue
            
        filepath = os.path.join(DATA_DIR, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
            # Determine type from filename
            base_name = filename.replace(".json", "")
            
            if "tarot" in base_name:
                # Handle tarot separately
                if isinstance(data, list):
                    master_db["tarot"].extend(data)
                else:
                    master_db["tarot"].append(data)
                continue

            # Handle oracles
            if base_name in ORACLE_TYPES:
                type_key = base_name
            else:
                # Some files might be subsets like gy1, mz1
                if base_name.startswith("gy"): type_key = "guanyin100"
                elif base_name.startswith("mz"): type_key = "mazu60"
                else: type_key = base_name
            
            if type_key not in master_db["oracles"]:
                master_db["oracles"][type_key] = []
            
            if isinstance(data, list):
                # Check for duplicates by ID
                existing_ids = {item['id'] for item in master_db["oracles"][type_key]}
                for item in data:
                    if item.get('id') not in existing_ids:
                        # Ensure fields are present
                        item['type'] = type_key
                        master_db["oracles"][type_key].append(item)
                        total_count += 1
            else:
                master_db["oracles"][type_key].append(data)
                total_count += 1
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    # Remove duplicates from tarot
    seen_tarot = set()
    unique_tarot = []
    for card in master_db["tarot"]:
        name = card.get("name")
        if name not in seen_tarot:
            unique_tarot.append(card)
            seen_tarot.add(name)
    master_db["tarot"] = unique_tarot

    # Save output
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(master_db, f, ensure_ascii=False, indent=2)
        
    print(f"Master DB created at {OUTPUT_FILE}")
    print(f"Total Oracles: {total_count}")
    print(f"Total Tarot Cards: {len(master_db['tarot'])}")

if __name__ == "__main__":
    consolidate()
