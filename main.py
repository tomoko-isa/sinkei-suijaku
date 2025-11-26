# 定数の定義 --- (*1)
CARD_W, CARD_H = 239, 335  # 素材画像のカード1枚のサイズ
COL, ROW = 4, 5  # 描画先の列数と行数
# 描画先のカード1枚のサイズを計算
DES_W = 380 // COL  # 描画先のカード1枚の幅
DES_H = int(DES_W / CARD_W * CARD_H)  # 描画先のカード1枚の高さ

# 特殊カードのIDを定義 --- (*2)
CARD_BACK_ID = 53  # 裏向きカードのID
CARD_NONE_ID = 56  # 既に取られたカードのID
DELAY_NEXT_MS = 2000  # 次の処理までの遅延時間(ミリ秒)

# グローバル変数 --- (*3)
cards = []
game = {"first": None, "second": None, "score": 0}

def game_start():
    """ゲームを開始する"""  # --- (*4)
    global cards, game
    # クローバーとダイヤのAから10のカードを用意
    cards = list(range(0, 10)) + list(range(13*1, 13*1+10))
    shuffle_list(cards)
    # ゲーム変数の初期化
    game = {"first": None, "second": None, "score": 0}
    q_text("#title", "神経衰弱")
    q_text("#info", "カードを2枚選んでペアを見つけてください！")
    draw_cards()

def check_card(index):
    """カードが選ばれた"""  # --- (*5)
    if cards[index] == CARD_NONE_ID:
        return  # 既に取られたカードなら無視
    if game["first"] is None:  # 最初のカードを選択 --- (*6)
        game["first"] = index
        q_text("#info", "2枚目のカードを選んでください")
    elif game["second"] is None:  # 2枚目のカードを選択 --- (*7)
        if game["first"] == index:
            return  # 同じカードは選べない
        game["second"] = index
        check_pair_selected()  # ペアが見つかったか?

def check_pair_selected():
    """ペアが選ばれているか?"""  # --- (*8)
    cno1 = cards[game["first"]] % 13
    cno2 = cards[game["second"]] % 13
    if cno1 == cno2:
        q_text("#info", "ペアが見つかりました!")
        game["score"] += 1
        set_timeout(handle_pair_matched, DELAY_NEXT_MS)
    else:
        q_text("#info", "ペアが違います。もう一度選んでください")
        set_timeout(handle_pair_mismatch, DELAY_NEXT_MS)
    draw_cards()  # カードを捲ったことを反映

def handle_pair_matched():
    """ペアが揃った後の処理"""  # --- (*9)
    # 山札からカードを取り除く
    cards[game["first"]] = CARD_NONE_ID
    cards[game["second"]] = CARD_NONE_ID
    # ユーザーの選択をリセット
    game["first"] = None
    game["second"] = None
    if game["score"] == len(cards) // 2:
        q_text("#info", "全部揃いました！ゲームクリア！")
        set_timeout(game_start, DELAY_NEXT_MS)

def handle_pair_mismatch():
    """ペアが違った後の処理"""  # --- (*10)
    # ユーザーの選択をリセット
    game["first"] = None
    game["second"] = None
    q_text("#info", "1枚目のカードを選んでください")
    draw_cards()

# 初回は自動的にゲームを開始 --- (*11)
set_timeout(game_start, 500)