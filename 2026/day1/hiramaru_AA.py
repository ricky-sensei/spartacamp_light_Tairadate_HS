# ひらまるを、文字だけで描くプログラム
# serifu の中身を変えると、吹き出しのセリフが変わるよ

serifu = "Let's プログラミング!"
fuki_haba = 26

# 絵のデータ
# 「13_」は「空白を13個」、「2#」は「#を2個」という意味
e = [
    "13_ 1\\",
    "14_ 1\\",
    "1= 1% 1+ 12_ 1\\",
    "60_ 1- 1% 2# 1:",
    "50_ 1. 1: 1. 1_ 1. 1% 4# 1- 1: 1* 1.",
    "49_ 4: 1- 4_ 1. 1+ 1# 1% 1# 1% 1.",
    "47_ 9: 2_ 1= 1: 1_ 1+ 1# 1* 1#",
    "36_ 2: 2- 4: 2_ 11- 1+ 5: 2- 1: 1-",
    "36_ 1: 1. 5: 1- 15: 1- 6: 1-",
    "36_ 4: 1- 21: 1- 3: 1-",
    "29_ 2. 5_ 2: 1- 23: 1. 1: 1- 1: 1- 6_ 1.",
    "27_ 1- 4# 1: 3_ 2- 26: 1. 1- 1. 4_ 4# 1*",
    "27_ 5# 1+ 1_ 1. 2- 29: 1- 1: 2_ 1: 5# 1:",
    "26_ 1: 6# 1- 9: 1. 2: 1@ 1% 6: 1. 2@ 10: 1- 2: 1= 5# 1%",
    "26_ 1= 6# 2: 1= 4: 4. 1- 5: 1+ 1# 1+ 5: 1- 4. 2: 2. 2- 1. 1- 5# 1%",
    "26_ 1- 5# 1% 2: 1- 2: 7. 5: 1- 1+ 1- 5: 6. 1: 4- 1: 6# 1%",
    "27_ 7# 1: 1- 1: 1- 6. 14: 6. 1: 4- 1: 6# 1*",
    "27_ 7# 1= 3- 1. 2: 2. 1- 2: 1- 1: 1. 2: 1_ 1: 1- 1. 1: 1- 1. 1: 1- 2. 2- 1. 1: 1- 1: 1- 7#",
    "27_ 1= 1% 6# 5: 11. 8_ 2. 7: 7# 1+",
    "28_ 1: 2% 2# 2% 1: 3_ 2. 18_ 1. 2: 1. 4_ 1: 2% 3# 1% 1#",
    "29_ 1: 4% 1# 1. 21_ 1. 1+ 1= 2- 1: 1- 1= 2_ 1. 1= 4% 1=",
    "31_ 1= 2% 1+ 1. 21_ 1= 1: 1* 1: 1* 1- 1+ 1: 1= 2_ 1- 3% 1.",
    "33_ 1% 1= 22_ 1= 1. 5+ 1_ 1= 2_ 1. 1%",
    "55_ 3. 1+ 1. 1: 1- 1_ 1: 1= 4_ 1.",
    "34_ 1. 17_ 4. 13_ 1.",
    "34_ 1: 14_ 5. 15_ 1.",
    "34_ 1: 11_ 5.",
]


# 1文字の見た目の幅を調べる（日本語は2、英数字や記号は1）
def moji_no_haba(moji):
    if ord(moji) > 255:
        return 2
    return 1


# 文字列全体の見た目の幅を、1文字ずつ足し算して調べる
def mojiretsu_no_haba(mojiretsu):
    goukei = 0
    for moji in mojiretsu:
        goukei = goukei + moji_no_haba(moji)
    return goukei


# 同じ文字を、指定された個数だけつなげる
def kurikaeshi(moji, kosuu):
    kekka = ""
    kaisuu = 0
    while kaisuu < kosuu:
        kekka = kekka + moji
        kaisuu = kaisuu + 1
    return kekka


# 「13」のような数字の文字列を、1けたずつ計算して整数にする
def suuji_ni_suru(mojiretsu):
    kazu = 0
    for moji in mojiretsu:
        hitoketa = ord(moji) - ord("0")
        kazu = kazu * 10 + hitoketa
    return kazu


# 「13_」を「空白13個」のように、元の文字の並びにもどす
def matome_wo_modosu(matome):
    suuji_no_bubun = ""
    kigou = ""
    for moji in matome:
        if "0" <= moji <= "9":
            suuji_no_bubun = suuji_no_bubun + moji
        else:
            kigou = moji
    if kigou == "_":
        kigou = " "
    return kurikaeshi(kigou, suuji_ni_suru(suuji_no_bubun))


# 1行ぶんのデータを、空白で区切って順番にもどしていく
def gyou_wo_modosu(gyou):
    kansei = ""
    matome = ""
    for moji in gyou + " ":
        if moji == " ":
            if matome != "":
                kansei = kansei + matome_wo_modosu(matome)
            matome = ""
        else:
            matome = matome + moji
    return kansei


# セリフの長さに合わせて、吹き出しを3行つくる
def fukidashi_wo_tsukuru(serifu):
    waku = "+" + kurikaeshi("-", fuki_haba) + "+"
    amari = fuki_haba - 1 - mojiretsu_no_haba(serifu)
    if amari < 0:
        amari = 0
    naka = "| " + serifu + kurikaeshi(" ", amari) + "|"
    return [waku, naka, waku]


# ここから実行
for line in fukidashi_wo_tsukuru(serifu):
    print(line)

for gyou in e:
    print(gyou_wo_modosu(gyou))

print("※ ひらまるのつもり笑")
