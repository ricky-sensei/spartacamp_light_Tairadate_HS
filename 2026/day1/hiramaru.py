# 円や楕円の式だけで、キャラクターを描くプログラム

haba = 80
takasa = 40
serifu = "Let's プログラミング!"

# 顔のまわりの花びら8枚の向き（右・右下・下・左下・左・左上・上・右上）
hanabira = [
    [1, 0], [0.7, 0.7], [0, 1], [-0.7, 0.7],
    [-1, 0], [-0.7, -0.7], [0, -1], [0.7, -0.7],
]


# (x, y) が、中心 (cx, cy)・横の半径 rx・縦の半径 ry の楕円の中にあるか
def daen(x, y, cx, cy, rx, ry):
    return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2


# (x, y) から、点A→点B の線分までの近さ（文字の横幅を半分として計算）
def senbun(x, y, ax, ay, bx, by):
    px = (x - ax) / 2
    py = y - ay
    vx = (bx - ax) / 2
    vy = by - ay
    t = (px * vx + py * vy) / (vx * vx + vy * vy)
    if t < 0:
        t = 0
    if t > 1:
        t = 1
    dx = px - vx * t
    dy = py - vy * t
    return (dx * dx + dy * dy) ** 0.5


def egaku(x, y):
    # 吹き出し
    fuki = daen(x, y, 20, 8, 19, 5)
    if fuki <= 1:
        if daen(x, y, 20, 8, 16.5, 3.9) > 1:
            if abs(y - 8) >= 4:
                return "-" if x % 3 != 2 else " "
            return ":"
        return " "
    if senbun(x, y, 33, 12, 41, 16) < 0.7:
        return "/"

    # 頭の上の芽
    if x == 54 and 3 <= y <= 6:
        return "|"
    if daen(x, y, 50, 3, 3, 1) <= 1 or daen(x, y, 58, 3, 3, 1) <= 1:
        return "@"

    # 顔（太陽）
    hx = (x - 54) / 2
    hy = y - 15
    if hx * hx + hy * hy <= 5.8 * 5.8:
        if daen(x, y, 51, 14, 0.6, 0.6) <= 1 or daen(x, y, 57, 14, 0.6, 0.6) <= 1:
            return "@"
        if daen(x, y, 54, 16, 0.6, 0.5) <= 1:
            return "v"
        if daen(x, y, 46, 16, 2.5, 1.2) <= 1 or daen(x, y, 62, 16, 2.5, 1.2) <= 1:
            return "o"
        return ":"
    for muki in hanabira:
        px = hx - muki[0] * 6.8
        py = hy - muki[1] * 6.8
        if px * px + py * py <= 2.6 * 2.6:
            return "*"

    # エプロンとマーク
    if daen(x, y, 61, 26, 3, 1.5) <= 1:
        return "@"
    if 21 <= y <= 33 and 44 <= x <= 66:
        if y == 21:
            return "~"
        if x == 44 or x == 66 or y == 33:
            return "+"
        return " "

    # 体・腕・足
    if daen(x, y, 55, 28, 24, 10) <= 1:
        return "#"
    if senbun(x, y, 68, 24, 74, 9) < 2.2:
        return "#"
    if senbun(x, y, 42, 25, 36, 33) < 2:
        return "#"
    if 36 <= y and (44 <= x <= 51 or 59 <= x <= 66):
        return "#"

    # 手をふる線
    if senbun(x, y, 77, 6, 79, 10) < 0.6 or senbun(x, y, 75, 3, 78, 7) < 0.6:
        return ")"
    return " "


# 全部のマスを計算して、絵を作る
e = []
for y in range(takasa):
    gyou = []
    for x in range(haba):
        gyou.append(egaku(x, y))
    e.append(gyou)

# 吹き出しの中にセリフを書く（日本語は2文字ぶんの幅をとる）
nagasa = 0
for c in serifu:
    nagasa = nagasa + (2 if ord(c) > 255 else 1)
x = 20 - nagasa // 2
for c in serifu:
    e[8][x] = c
    if ord(c) > 255:
        e[8][x + 1] = ""
        x = x + 2
    else:
        x = x + 1

for gyou in e:
    print("".join(gyou).rstrip())
