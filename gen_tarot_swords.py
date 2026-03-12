import json
import os

cards = []
for i in range(1, 15):
    cards.append({
        "id": f"swords_{i}",
        "type": "tarot",
        "name": "",
        "arcana": "minor",
        "suit": "swords",
        "number": i,
        "up": "",
        "rev": "",
        "advice": {
            "work": "保持清晰的頭腦與邏輯，果斷地做出決策，不要被情緒左右。",
            "love": "雙方需要理性的溝通，有話直說但要注意言詞，避免無謂的言語傷害。",
            "money": "理財需謹慎分析，看清合約細節，切勿盲目聽信他人。",
            "family": "遇到家庭爭執時，請用客觀講理的方式解決，避免情緒化的指責。",
            "other": "用你的智慧與理性斬斷眼前的混亂，真相只有一個。"
        }
    })

meanings = [
    ("寶劍王牌 (Ace of Swords)", "清晰的思考、真理、新計畫、決斷力、洞察力。", "混亂、判斷錯誤、溝通不良、缺乏遠見、殘酷。"),
    ("寶劍二 (Two of Swords)", "僵局、逃避現實、拒絕溝通、兩難的抉擇、維持表面和平。", "打破僵局、面對現實、做出決定、資訊過載。"),
    ("寶劍三 (Three of Swords)", "悲傷、心碎、背叛、痛苦的真相、分離。", "走出傷痛、療癒、釋懷、不再壓抑悲傷。"),
    ("寶劍四 (Four of Swords)", "休息、沉思、養精蓄銳、暫停行動、平靜。", "被迫行動、過勞、無法休息、從休養中恢復。"),
    ("寶劍五 (Five of Swords)", "失敗、惡性競爭、自私、兩敗俱傷、不擇手段的勝利。", "和解、認清失敗、停止無謂的爭端、放下仇恨。"),
    ("寶劍六 (Six of Swords)", "度過難關、漸入佳境、遠離悲傷、旅行、尋求平靜。", "無法前進、逃避問題、困在過去、延遲的旅程。"),
    ("寶劍七 (Seven of Swords)", "欺騙、隱瞞、逃避責任、偷偷摸摸、孤軍奮戰。", "真相大白、揭發謊言、改過自新、面對現實。"),
    ("寶劍八 (Eight of Swords)", "束縛、自我設限、被害妄想、無能為力、恐懼。", "掙脫束縛、重獲自由、解除恐懼、看清真相。"),
    ("寶劍九 (Nine of Swords)", "焦慮、噩夢、絕望、罪惡感、精神折磨。", "度過黑暗、正視恐懼、放下擔憂、向外求助。"),
    ("寶劍十 (Ten of Swords)", "徹底失敗、結束、被背叛、谷底、痛苦的終結。", "重生、最壞的已過、重新開始、從谷底攀升。"),
    ("寶劍侍者 (Page of Swords)", "機警、好奇、防備心、探聽消息、口齒伶俐。", "多嘴、造謠、缺乏防備、講話傷人、探人隱私。"),
    ("寶劍騎士 (Knight of Swords)", "迅速、果斷、直言不諱、衝鋒陷陣、缺乏耐性。", "魯莽、言詞傷人、思考不周、橫衝直撞。"),
    ("寶劍王后 (Queen of Swords)", "理性、獨立、冷靜、判斷力強、直言不諱的女性。", "殘酷、冷血、尖酸刻薄、孤僻、不近人情。"),
    ("寶劍國王 (King of Swords)", "專業、權威、邏輯清晰、冷靜的領導者、公正。", "專制、不通人情、濫用權力、冷漠無情。")
]

for i, (name, up, rev) in enumerate(meanings):
    cards[i]["name"] = name
    cards[i]["up"] = up
    cards[i]["rev"] = rev

with open(r"c:\Users\yyutingliu\Downloads\抽籤\data\tarot_swords.json", 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print("Tarot Swords (14 cards) generated.")
