# リッキーとガッキーが、決着がつくまで自動で戦うプログラム
# seed の数字を変えると、戦いの流れが変わるよ

seed = 37

ricky = {
    "名前": "リッキー",
    "HP": 700,
    "攻撃力": 100,
    "防御力": 80,
    "必殺技": "スパルタキック",
}
gacky = {
    "名前": "ガッキー",
    "HP": 600,
    "攻撃力": 200,
    "防御力": 80,
    "必殺技": "関西弁ツッコミ",
}


# サイコロの代わり：計算だけで、それっぽくバラバラな数字を作る
def dice(kosuu):
    global seed
    seed = (seed * 1103515245 + 12345) % 2147483648
    return seed // 65536 % kosuu


def attack(semeru, mamoru):
    me = dice(6) + 1
    if me == 6:
        # 6が出たら必殺技。防御を無視して大ダメージ
        damage = semeru["攻撃力"] + dice(50)
        print(semeru["名前"] + "の" + semeru["必殺技"] + "!!!")
    elif me == 1:
        damage = 0
        print(semeru["名前"] + "のこうげき！...しかし、ミス！")
    else:
        damage = semeru["攻撃力"] - mamoru["防御力"] + dice(20)
        print(semeru["名前"] + "のこうげき！")
    if damage < 0:
        damage = 0
    mamoru["HP"] = mamoru["HP"] - damage
    if mamoru["HP"] < 0:
        mamoru["HP"] = 0
    print(mamoru["名前"] + "に" + str(damage) + "のダメージ（のこりHP:" + str(mamoru["HP"]) + "）")


print("=== " + ricky["名前"] + " VS " + gacky["名前"] + " ===")
turn = 1
while ricky["HP"] > 0 and gacky["HP"] > 0:
    print("")
    print("--- ターン" + str(turn) + " ---")
    attack(ricky, gacky)
    if gacky["HP"] == 0:
        break
    attack(gacky, ricky)
    turn = turn + 1

print("")
if ricky["HP"] > 0:
    print(ricky["名前"] + "の勝利！")
else:
    print(gacky["名前"] + "の勝利！")
