# 年齢から料金区分を返す関数（テスト対象）
def get_fee_category(age):
    if age < 0:                                     # マイナスかどうか
        raise ValueError("0より小さい数字は入力できません")
    if age < 13:
        return "子ども"
    elif age < 65:
        return "大人"
    else:
        return "シニア"