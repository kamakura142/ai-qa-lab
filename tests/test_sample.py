import pytest

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


# ② 正常系テスト：境界値分析（0、12と13、64と65）
@pytest.mark.parametrize("age, expected", [
    (0, "子ども"),     # 有効な最小の年齢
    (12, "子ども"),    # 子どもである最後の年齢
    (13, "大人"),      # 大人になる最初の年齢
    (64, "大人"),      # 大人である最後の年齢
    (65, "シニア"),    # シニアになる最初の年齢
])
def test_子供大人シニア判別(age, expected):
    assert get_fee_category(age) == expected

# ③ 異常系テスト：マイナスはエラーになる
def test_マイナスはエラー():
    with pytest.raises(ValueError):                    # どのエラーが出るはずか
       get_fee_category(-1)                                   # 関数を -1 で呼ぶ