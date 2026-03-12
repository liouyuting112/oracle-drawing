import json
import os

cards = []
for i in range(1, 15):
    cards.append({
        "id": f"pentacles_{i}",
        "type": "tarot",
        "name": "",
        "arcana": "minor",
        "suit": "pentacles",
        "number": i,
        "up": "",
        "rev": "",
        "advice": {
            "work": "腳踏實地地建立你的專業基礎，現在的努力將為未來帶來豐碩的回報。",
            "love": "這是一段需要穩定與承諾的關係，透過實質的關心與照顧來表達愛意。",
            "money": "保守理財，注重長期的規劃與投資，穩健累積你的財富。",
            "family": "為家人提供堅實的物質基礎與安全感，共同經營美好的生活品質。",
            "other": "享受努力工作帶來的豐收，感謝大地的滋養與物質的豐盛。"
        }
    })

meanings = [
    ("金幣王牌 (Ace of Pentacles)", "新的財源、繁榮、穩固的開始、物質的回報、好機會。", "錯失良機、財務損失、基礎不穩、貪婪、投資失利。"),
    ("金幣二 (Two of Pentacles)", "財務平衡、靈活調度、波動中求穩、兼顧多事。", "財務失衡、蠟燭兩頭燒、缺乏彈性、調度失敗。"),
    ("金幣三 (Three of Pentacles)", "團隊合作、專業技能、被認可、建立基礎、學習。", "合作破裂、半途而廢、缺乏專業、無人賞識。"),
    ("金幣四 (Four of Pentacles)", "掌控、吝嗇、保守、安全感、害怕失去、守財奴。", "破財、慷慨解囊、解除防備、揮霍無度、失去控制。"),
    ("金幣五 (Five of Pentacles)", "貧困、孤立無援、經濟危機、健康不佳、缺乏精神寄託。", "財務好轉、獲得救助、度過難關、重拾信仰。"),
    ("金幣六 (Six of Pentacles)", "慷慨、施與受、慈善、獲得資助、公平的分配。", "自私、分配不公、被敲竹槓、假慈善、債務。"),
    ("金幣七 (Seven of Pentacles)", "評估、等待收成、反思、長遠規劃、耐心。", "缺乏耐心、投資無回報、半途而廢、不滿現狀。"),
    ("金幣八 (Eight of Pentacles)", "專注、勤奮、精益求精、工匠精神、努力工作。", "粗心大意、缺乏動力、工作乏味、品質低劣。"),
    ("金幣九 (Nine of Pentacles)", "豐收、優雅、獨立、享受成果、物質充裕。", "揮霍無度、過度依賴別人、被物質綁架、外強中乾。"),
    ("金幣十 (Ten of Pentacles)", "家族財富、傳承、長期的繁榮、穩固的家庭、遺產。", "家庭紛爭、失去財產、財務風險、傳統包袱。"),
    ("金幣侍者 (Page of Pentacles)", "好學、踏實、新的投資機會、勤奮的學徒、實體禮物。", "不切實際、怠惰、錯失投資良機、浪費金錢。"),
    ("金幣騎士 (Knight of Pentacles)", "可靠、勤奮、穩定進展、有責任感、保守。", "死板、固執、進度停滯、缺乏靈活性、工作狂。"),
    ("金幣王后 (Queen of Pentacles)", "慷慨、溫暖、實際、善於理財、享受生活的女性。", "自私、物質主義、過度溺愛、貪婪、不善理財。"),
    ("金幣國王 (King of Pentacles)", "富裕、權威、事業成功、可靠的領導者、享受物質享受。", "貪婪、腐敗、固執、濫用財富、唯物主義。")
]

for i, (name, up, rev) in enumerate(meanings):
    cards[i]["name"] = name
    cards[i]["up"] = up
    cards[i]["rev"] = rev

with open(r"c:\Users\yyutingliu\Downloads\抽籤\data\tarot_pentacles.json", 'w', encoding='utf-8') as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print("Tarot Pentacles (14 cards) generated.")
