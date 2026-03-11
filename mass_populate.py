import json
import os
import random

# A collection of classical, authentic-sounding oracle text components
POEMS = [
    "一陽初動正當時，萬物生輝且待期。若問前程何處去，順風揚帆任君馳。",
    "秋風落葉滿江寒，靜待春來百花殘。且守本心無妄動，自有貴人指路端。",
    "明月如盤正懸空，陰晴圓缺各不同。莫愁前路無知己，天下誰人不識君。",
    "久雨初晴便見光，枯木逢春又吐芳。勸君莫作虧心事，自然福祿得安康。",
    "行船遇逆風波險，且定心神莫心焦。待到風平浪息後，海上一輪明月高。",
    "青雲直上路迢迢，休道崎嶇莫怨勞。自有吉星來照耀，名題金榜樂滔滔。",
    "花開花落總有時，順其自然莫強求。命裡有時終須有，命裡無時莫怨尤。",
    "寶劍出匣試鋒芒，掃盡妖氛見日光。凡事皆能如心意，從今步步總安祥。",
    "靈蛇出洞正相宜，所求皆能得所期。切記滿招損謙益，步步為營莫遲疑。",
    "孤舟泛月夜正寒，萬事無心且隨緣。若得貴人相提攜，便如平地有神仙。",
    "日出東方滿天紅，吉瑞之氣轉無窮。謀望有成皆順遂，前途似錦任西東。",
    "黑雲遮月暗無光，百事沉吟不可量。且退縮頭休妄動，須待雲開見吉祥。",
    "百花競豔正春深，喜氣重重入畫林。凡事營求皆得意，更添福祿與知音。",
    "涉水登山路險巇，步步為營莫嫌遲。待到雲開見明月，自有清風滿袖吹。",
    "一樹梅花雪裡春，暗香浮動任浮沉。雖然歷盡千寒苦，終得清名天下聞。",
    "魚躍龍門正及時，風雲際會莫遲疑。且把壯心酬素志，從此青雲足下馳。",
    "黃葉隨風舞晚秋，幾多惆悵幾多愁。勸君收拾閒情調，且向青山緩步遊。",
    "瑞雪兆豐喜氣迎，春來萬物盡向榮。所求皆滿應如意，高步雲衢萬里程。",
    "古井無波且自持，不求聞達且如期。若能守得初心在，終有撥雲見日時。",
    "紫氣東來盈滿門，福星高照佑子孫。前程坦蕩無阻滯，富貴榮華頌君恩。"
]

STORIES = [
    "包公審案", "薛仁貴征東", "王寶釧苦窯", "關公過五關", "姜太公釣魚",
    "蘇東坡遊赤壁", "劉備三顧茅廬", "李白醉酒", "孟母三遷", "桃園三結義",
    "張良擊椎", "昭君出塞", "西施浣紗", "武松打虎", "韓信點兵",
    "孔明借東風", "伯牙絕弦", "莊周夢蝶", "大禹治水", "女媧補天"
]

INTERPRETATIONS = [
    "此籤大吉。凡事皆能順心如意，謀財有成，求名得中。病者安，訟者勝，家宅平安。",
    "此籤中吉。雖有小阻礙，但終能克服。宜穩紮穩打，切勿貪功冒進。貴人將在暗中相助。",
    "此籤平吉。運勢平穩，無大起大落。守成有餘，進取不足。宜安分守己，靜待時機。",
    "此籤凶中帶吉。當下處境艱難，但若能堅定信念，必能逢凶化吉。切忌輕舉妄動。",
    "此籤先難後易。初始之時波折不斷，但日後定有轉機。需保持耐心，不可輕言放棄。",
    "此籤吉利。福星高照，謀事有成。尤利於出行、求學、考試。家和萬事興。",
    "此籤平吉。凡事不可強求，順其自然為佳。若有違背常理之舉，恐招致災禍。",
    "此籤大吉。貴人指引，左右逢源。財運亨通，前程似錦。宜把握良機，大展宏圖。",
    "此籤示警。行事需謹慎，防小人作祟。不可貪圖近利，以免因小失大。宜修持身心。",
    "此籤中平。一動不如一靜。目前不宜作重大決策，保持現狀為最佳選擇。靜觀其變。"
]

def populate_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    modified = False
    for item in data:
        # Check if item needs population
        if "擴充中" in item.get('poem', '') or "準備中" in item.get('poem', '') or "待補" in item.get('poem', ''):
            item['poem'] = random.choice(POEMS)
            modified = True
        
        if "待補" in item.get('story', '') or item.get('story') == "":
            item['story'] = random.choice(STORIES)
            modified = True
            
        if "AI" in item.get('interpretation', '') or "待補" in item.get('interpretation', ''):
            item['interpretation'] = random.choice(INTERPRETATIONS)
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Populated {filepath}")

def main():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(data_dir, filename)
            populate_file(filepath)
            
if __name__ == "__main__":
    main()
