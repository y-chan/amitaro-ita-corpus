import copy
import uuid
import json

vowel_phoneme_list = ["a", "i", "u", "e", "o", "N", "A", "I", "U", "E", "O", "cl"]
_mora_list_minimum = [
    ["ヴォ", "v", "o"],
    ["ヴェ", "v", "e"],
    ["ヴィ", "v", "i"],
    ["ヴァ", "v", "a"],
    ["ヴ", "v", "u"],
    ["ン", "", "N"],
    ["ワ", "w", "a"],
    ["ロ", "r", "o"],
    ["レ", "r", "e"],
    ["ル", "r", "u"],
    ["リョ", "ry", "o"],
    ["リュ", "ry", "u"],
    ["リャ", "ry", "a"],
    ["リェ", "ry", "e"],
    ["リ", "r", "i"],
    ["ラ", "r", "a"],
    ["ヨ", "y", "o"],
    ["ユ", "y", "u"],
    ["ヤ", "y", "a"],
    ["モ", "m", "o"],
    ["メ", "m", "e"],
    ["ム", "m", "u"],
    ["ミョ", "my", "o"],
    ["ミュ", "my", "u"],
    ["ミャ", "my", "a"],
    ["ミェ", "my", "e"],
    ["ミ", "m", "i"],
    ["マ", "m", "a"],
    ["ポ", "p", "o"],
    ["ボ", "b", "o"],
    ["ホ", "h", "o"],
    ["ペ", "p", "e"],
    ["ベ", "b", "e"],
    ["ヘ", "h", "e"],
    ["プ", "p", "u"],
    ["ブ", "b", "u"],
    ["フォ", "f", "o"],
    ["フェ", "f", "e"],
    ["フィ", "f", "i"],
    ["ファ", "f", "a"],
    ["フ", "f", "u"],
    ["ピョ", "py", "o"],
    ["ピュ", "py", "u"],
    ["ピャ", "py", "a"],
    ["ピェ", "py", "e"],
    ["ピ", "p", "i"],
    ["ビョ", "by", "o"],
    ["ビュ", "by", "u"],
    ["ビャ", "by", "a"],
    ["ビェ", "by", "e"],
    ["ビ", "b", "i"],
    ["ヒョ", "hy", "o"],
    ["ヒュ", "hy", "u"],
    ["ヒャ", "hy", "a"],
    ["ヒェ", "hy", "e"],
    ["ヒ", "h", "i"],
    ["パ", "p", "a"],
    ["バ", "b", "a"],
    ["ハ", "h", "a"],
    ["ノ", "n", "o"],
    ["ネ", "n", "e"],
    ["ヌ", "n", "u"],
    ["ニョ", "ny", "o"],
    ["ニュ", "ny", "u"],
    ["ニャ", "ny", "a"],
    ["ニェ", "ny", "e"],
    ["ニ", "n", "i"],
    ["ナ", "n", "a"],
    ["ドゥ", "d", "u"],
    ["ド", "d", "o"],
    ["トゥ", "t", "u"],
    ["ト", "t", "o"],
    ["デョ", "dy", "o"],
    ["デュ", "dy", "u"],
    ["デャ", "dy", "a"],
    ["デェ", "dy", "e"],
    ["ディ", "d", "i"],
    ["デ", "d", "e"],
    ["テョ", "ty", "o"],
    ["テュ", "ty", "u"],
    ["テャ", "ty", "a"],
    ["ティ", "t", "i"],
    ["テ", "t", "e"],
    ["ツォ", "ts", "o"],
    ["ツェ", "ts", "e"],
    ["ツィ", "ts", "i"],
    ["ツァ", "ts", "a"],
    ["ツ", "ts", "u"],
    ["ッ", "", "cl"],
    ["チョ", "ch", "o"],
    ["チュ", "ch", "u"],
    ["チャ", "ch", "a"],
    ["チェ", "ch", "e"],
    ["チ", "ch", "i"],
    ["ダ", "d", "a"],
    ["タ", "t", "a"],
    ["ゾ", "z", "o"],
    ["ソ", "s", "o"],
    ["ゼ", "z", "e"],
    ["セ", "s", "e"],
    ["ズィ", "z", "i"],
    ["ズ", "z", "u"],
    ["スィ", "s", "i"],
    ["ス", "s", "u"],
    ["ジョ", "j", "o"],
    ["ジュ", "j", "u"],
    ["ジャ", "j", "a"],
    ["ジェ", "j", "e"],
    ["ジ", "j", "i"],
    ["ショ", "sh", "o"],
    ["シュ", "sh", "u"],
    ["シャ", "sh", "a"],
    ["シェ", "sh", "e"],
    ["シ", "sh", "i"],
    ["ザ", "z", "a"],
    ["サ", "s", "a"],
    ["ゴ", "g", "o"],
    ["コ", "k", "o"],
    ["ゲ", "g", "e"],
    ["ケ", "k", "e"],
    ["グヮ", "gw", "a"],
    ["グ", "g", "u"],
    ["クヮ", "kw", "a"],
    ["ク", "k", "u"],
    ["ギョ", "gy", "o"],
    ["ギュ", "gy", "u"],
    ["ギャ", "gy", "a"],
    ["ギェ", "gy", "e"],
    ["ギ", "g", "i"],
    ["キョ", "ky", "o"],
    ["キュ", "ky", "u"],
    ["キャ", "ky", "a"],
    ["キェ", "ky", "e"],
    ["キ", "k", "i"],
    ["ガ", "g", "a"],
    ["カ", "k", "a"],
    ["オ", "", "o"],
    ["エ", "", "e"],
    ["ウォ", "w", "o"],
    ["ウェ", "w", "e"],
    ["ウィ", "w", "i"],
    ["ウ", "", "u"],
    ["イェ", "y", "e"],
    ["イ", "", "i"],
    ["ア", "", "a"],
]

openjtalk_mora2text = {
    consonant + vowel: text for [text, consonant, vowel] in _mora_list_minimum
}

def mora_to_text(mora: str) -> str:
    if mora[-1:] in ["A", "I", "U", "E", "O"]:
        # 無声化母音を小文字に
        mora = mora[:-1] + mora[-1].lower()
    if mora in openjtalk_mora2text:
        return openjtalk_mora2text[mora]
    else:
        return mora

with open("index.csv") as f:
    labels = f.read().split("\n")

project_base = {
    "appVersion": "0.10.4",
    "audioKeys": [],
    "audioItems": {}
}
query_base = {
    "speedScale": 1,
    "pitchScale": 0,
    "intonationScale": 1,
    "volumeScale": 1,
    "prePhonemeLength": 0.1,
    "postPhonemeLength": 0.1,
    "outputSamplingRate":24000,
    "outputStereo": False,
    "kana": ""
}

with open("./transcript.txt", encoding="utf8") as ts:
    transcript = [s.split(",")[0] for s in ts.read().split("\n")]

project = copy.deepcopy(project_base)

for i in range(0, len(labels), 2):
    if i != 0 and i % 100 == 0:
        with open(f"project{(i//2) - 49}-{i//2}.vvproj", mode="w", encoding="utf8") as pjf:
            pjf.write(json.dumps(project, ensure_ascii=False))
            project = copy.deepcopy(project_base)
    phonemes = labels[i].split()
    accents = labels[i+1].replace(", ", ",").replace("   ", " ").replace("  ", " ").split()
    phonemes[0] = phonemes[0].split(",")[1]
    accents[0] = accents[0].split(",")[1]
    accent_phrases = []
    accent_phrase = {}
    count = 0
    mora = {}
    for j, phoneme in enumerate(phonemes):
        if accent_phrase.get("moras") is None:
            accent_phrase["moras"] = []
        if phoneme == "pau":
            if accent_phrase.get("accent") is None:
                accent_phrase["accent"] = count
            accent_phrase["pauseMora"] = {
                "vowel": phoneme,
                "vowelLength": 0,
                "pitch": 0,
                "text": "、"
            }
            accent_phrase["isInterrogative"] = False
            accent_phrases.append(copy.deepcopy(accent_phrase))
            accent_phrase = {}
            count = 0
            continue

        if phoneme in vowel_phoneme_list:
            mora["vowel"] = phoneme
            mora["vowelLength"] = 0
            if mora.get("consonant") is not None:
                text = mora_to_text(mora["consonant"] + phoneme)
            else:
                text = mora_to_text(phoneme)
            mora["text"] = text
            mora["pitch"] = 0
            count += 1
            end = accents[j] in ["#", "?"]
            if "]" == accents[j]:
                accent_phrase["accent"] = count
            elif end and accent_phrase.get("accent") is None:
                accent_phrase["accent"] = count
            accent_phrase["moras"].append(copy.deepcopy(mora))
            if end:
                accent_phrase["isInterrogative"] = accents[j] == "?"
                accent_phrases.append(copy.deepcopy(accent_phrase))
                accent_phrase = {}
                count = 0
            mora = {}
        else:
            mora["consonant"] = phoneme
            mora["consonantLength"] = 0
    query = copy.deepcopy(query_base)
    query["accentPhrases"] = accent_phrases
    key = str(uuid.uuid4())
    project["audioKeys"].append(key)
    project["audioItems"][key] = {
        # "text": transcript[i].split(":")[1],
        "text": transcript[i//2],
        "styleId": 0,
        "query": query
    }

with open(f"project{(i//2) - 23}-{(i+2)//2}.vvproj", mode="w", encoding="utf8") as pjf:
    pjf.write(json.dumps(project, ensure_ascii=False))
