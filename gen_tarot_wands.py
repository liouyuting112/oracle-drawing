import json
import os

cards = []
for i in range(1, 15):
    name = f"權杖{i}" if i <= 10 else ["侍者 (Page)", "騎士 (Knight)", "王后 (Queen)", "國王 (King)"][i-11]
    if i > 10: name = f"權杖{name}"
    cards.append({
        "id": f"wands_{i}",
        "type": "tarot",
        "name": name,
        "arcana": "minor",
        "suit": "wands",
        "number": i,
        "up": "行動力、熱情、創造力、新的開始、旅行。" if i == 1 else "計劃、決定、擴展視野。", # Simplified for demo brevity, will flesh out.
        "rev": "缺乏動力、計畫延遲、創造力受阻。",
        "advice": {
            "work": "保持熱情，主動出擊，你的行動力將決定成功。",
            "love": "感情充滿火花，需要兩人共同創造新鮮感。",
            "money": "財富來自於你的積極開創與冒險精神。",
            "family": "鼓勵家人共同參與戶外活動或新的計畫。",
            "other": "跟隨你的直覺與熱情，大膽邁出第一步。"
        }
    })

# Flesh out Wands 1 to 14
meanings = [
    ("權杖王牌 (Ace of Wands)", "新的靈感、熱情、行動力、創造力的開始、潛力。", "缺乏動力、計畫延宕、錯失良機、熱情消退。"),
    ("權杖二 (Two of Wands)", "計畫、決定、擴展視野、未來的規劃、出國。", "害怕未知、計畫受阻、猶豫不決、眼光短淺。"),
    ("權杖三 (Three of Wands)", "合作、遠見、擴張、貿易、等待船隻歸來、自信。", "合作失敗、好高騖遠、進度落後、缺乏遠見。"),
    ("權杖四 (Four of Wands)", "歡慶、和諧、穩固的基礎、回鄉、結婚、完成階段性目標。", "短暫的快樂、基礎不穩、家庭紛爭、無法享受成果。"),
    ("權杖五 (Five of Wands)", "競爭、衝突、意見不合、腦力激盪、混亂的局面。", "惡性競爭、逃避衝突、內在矛盾、兩敗俱傷。"),
    ("權杖六 (Six of Wands)", "勝利、成功、榮耀、被認可、自信滿滿、好消息。", "短暫的成功、驕傲自大、缺乏認可、被人排擠。"),
    ("權杖七 (Seven of Wands)", "防禦、堅守立場、面臨挑戰、勇氣、不屈不撓。", "放棄抵抗、不知所措、妥協、被壓力擊垮。"),
    ("權杖八 (Eight of Wands)", "迅速、行動、快速進展、旅行、突如其來的消息。", "進展緩慢、延遲、溝通不良、衝動行事。"),
    ("權杖九 (Nine of Wands)", "防備、疲憊、堅持到底、最後的考驗、受傷但未倒下。", "過度防備、固執、無法堅持、創傷後遺症。"),
    ("權杖十 (Ten of Wands)", "壓力、重擔、責任過重、辛苦建立的成就、過勞。", "壓力崩潰、推卸責任、無法負荷、白費力氣。"),
    ("權杖侍者 (Page of Wands)", "好奇心、探索、新計畫的萌芽、熱情的年輕人、好消息。", "三分鐘熱度、魯莽、壞消息、缺乏行動力。"),
    ("權杖騎士 (Knight of Wands)", "行動力、衝勁、冒險、熱情奔放、旅行、急躁。", "魯莽行事、缺乏計畫、脾氣暴躁、半途而廢。"),
    ("權杖王后 (Queen of Wands)", "自信、魅力、獨立、溫暖、熱情如火的女強人。", "情緒化、嫉妒、專橫、跋扈、缺乏自信。"),
    ("權杖國王 (King of Wands)", "領導力、遠見、權威、開創者、具有影響力。", "專制、獨裁、脾氣暴躁、要求過高、自以為是。")
]

for i, (name, up, rev) in enumerate(meanings):
    cards[i]["name"] = name
    cards[i]["up"] = up
    cards[i]["rev"] = rev

with open(r"c:\Users\yyutingliu\Downloads\抽籤\data\tarot_wands.json", 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print("Tarot Wands (14 cards) generated.")
