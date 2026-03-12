import os
import json

DATA_DIR = r"c:\Users\yyutingliu\Downloads\抽籤\data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def save_json(filename, data):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

OTHER_SYSTEMS = {
    "guandi100": {"name": "雷雨師一百籤（關帝/城隍）", "count": 100},
    "tudigong28": {"name": "土地公廿八籤", "count": 28},
    "yuelao": {"name": "月老靈籤", "count": 100},
    "sevenkings60": {"name": "東港七王爺", "count": 60},
    "zhuge384": {"name": "諸葛神算", "count": 384},
    "baosheng60": {"name": "保生大帝", "count": 60},
    "qingshui50": {"name": "清水祖師", "count": 50},
    "luzu100": {"name": "呂祖一百籤", "count": 100},
    "luzu60": {"name": "呂仙祖六十籤", "count": 60},
    "zhusheng30": {"name": "註生娘娘", "count": 30},
    "beidi51": {"name": "北帝", "count": 51},
    "fourface30": {"name": "四面佛", "count": 30},
    "caishin100": {"name": "五路財神", "count": 100},
    "beidi100": {"name": "北帝一百籤", "count": 100},
    "guanyin28": {"name": "觀音廿八籤", "count": 28},
    "guanyin24": {"name": "觀音廿四籤", "count": 24},
    "zodiac28": {"name": "二十八星宿", "count": 28},
    "pienchu100": {"name": "扁鵲神醫藥籤", "count": 100},
    "yaoqian50": {"name": "藥籤50", "count": 50},
    "yaoqian200": {"name": "藥籤200", "count": 200},
    "lukang100": {"name": "鹿港天后宮", "count": 100},
    "penghu100": {"name": "澎湖天后宮", "count": 100},
    "zhuge64": {"name": "諸葛孔明六十四籤（金錢卦）", "count": 64},
    "zhuge32": {"name": "諸葛孔明三十二籤（金錢卦）", "count": 32},
    "chenghuang28": {"name": "城隍廿八籤", "count": 28} # Added this because mass_populate had it
}

for prefix, info in OTHER_SYSTEMS.items():
    amount = info["count"]
    sys_name = info["name"]
    lots = []
    
    for i in range(1, amount + 1):
        lot = {
            "id": i,
            "type": prefix,
            "no": f"第{i}籤",
            "level": "中平" if i % 2 == 0 else "中吉",
            "poem": f"{sys_name}玄機妙算第{i}籤，\n誠心祈求指迷津。\n萬事隨緣莫強求，\n福運自然降門庭。",
            "story": f"{sys_name}典故故事第{i}則",
            "interpretation": f"這支籤代表著順其自然、不要強求。在工作上建議做好份內之事，暫時不要輕舉妄動；感情方面則需要多些耐心與包容，不宜急躁。關於財運，目前的運勢平平，守成即可，不適合進行高風險的投資。只要心存善念，問題自然能迎刃而解。",
            "source": sys_name
        }
        lots.append(lot)
    
    save_json(f"{prefix}.json", lots)
    print(f"Generated {prefix}.json with {amount} items.")

print("Finished generating generic 25 oracles.")
