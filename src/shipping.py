# 会員区分と購入金額から送料を返す関数
# is_member: 会員なら True、一般なら False
# amount: 購入金額（円）
def calculate_shipping(is_member, amount):
    if is_member:
        if amount >= 5000:
            return 0
        else:
            return 300
    else:
        if amount >= 5000:
            return 300
        else:
            return 500