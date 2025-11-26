"""カード描画モジュール (draw.py)"""
# キャンバスとコンテキストの取得 --- (*1)
canvas = q("#canvas")
context = canvas.getContext("2d")

def draw_cards():
    """カードを描画する"""  # --- (*2)
    # スコアを表示
    q_text("#title", f"神経衰弱 ({game['score']}点)")
    # カードを描画
    for i, card in enumerate(cards):
        # 描画位置を計算 --- (*3)
        x = (i % COL) * DES_W
        y = (i // COL) * DES_H
        # どのカードを描画するか? --- (*4)
        if card == CARD_NONE_ID:  # 既に取られたカード
            context.clearRect(x, y, DES_W, DES_H)
            continue
        if i not in (game["first"], game["second"]):
            card = CARD_BACK_ID  # 裏向きカードをセット
        # カード素材の位置を確認 --- (*5)
        sx = (card % 13) * CARD_W
        sy = (card // 13) * CARD_H
        context.drawImage(
            q("img#cards"),  # カード素材の画像要素
            sx, sy, CARD_W, CARD_H,  # 素材の切り出し位置とサイズ
            x, y, DES_W, DES_H,  # 描画先の位置とサイズ
        )