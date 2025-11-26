"""クリック処理モジュール (click.py)"""
def card_click(event):
    """カードがクリックされた時の処理"""  # --- (*1)
    # クリックされた位置を取得 --- (*2)
    rect = canvas.getBoundingClientRect()
    x = int(event.clientX - rect.left)
    y = int(event.clientY - rect.top)
    # クリックされたカードを特定 --- (*3)
    click_col = x // DES_W
    click_row = y // DES_H
    index = click_row * COL + click_col
    if index >= len(cards):
        return  # 範囲外
    check_card(index)
    draw_cards()

# クリックイベントの設定 --- (*4)
canvas.addEventListener("click", card_click)