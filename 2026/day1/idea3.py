# 掛け算と足し算だけで、ふしぎな模様を描くプログラム
# 「マンデルブロ集合」という、数学の世界で有名な図形だよ

# 表示する大きさ（文字数）
haba = 78
takasa = 32

# 模様のどのあたりを描くか
hidari = -2.2
migi = 0.8
ue = 1.2
shita = -1.2

# 計算をくり返す回数（多いほど細かくなるけど、時間がかかる）
kurikaeshi = 60

# 計算がはやく「とびだした」場所ほど、うすい文字で描く
iro = {
    0: ".",
    1: ":",
    2: "-",
    3: "=",
    4: "+",
    5: "*",
    6: "%",
    7: "#",
    8: "&",
    9: "@",
}

for y in range(takasa):
    line = ""
    for x in range(haba):
        # 画面の位置を、模様の座標に変換する
        a = hidari + (migi - hidari) * x / haba
        b = ue - (ue - shita) * y / takasa

        # z = z × z + c をくり返して、遠くへとびだすか調べる
        zr = 0.0
        zi = 0.0
        kaisuu = 0
        while kaisuu < kurikaeshi and zr * zr + zi * zi <= 4:
            atarashii_zr = zr * zr - zi * zi + a
            zi = 2 * zr * zi + b
            zr = atarashii_zr
            kaisuu = kaisuu + 1

        if kaisuu == kurikaeshi:
            # 最後までとびださなかった場所は、こい文字でぬりつぶす
            line = line + iro[9]
        else:
            line = line + iro[kaisuu % 9]
    print(line)

print("")
print("掛け算と足し算だけで、この模様が描けたよ！")
print("hidari や migi の数字を変えると、模様を拡大できるよ")
