# 年齢から料金区分を返す関数（テスト対象）
def get_fee_category(age):
    if age < 13:
        return "子ども"
    elif age < 65:
        return "大人"
    else:
        return "シニア"


# 境界値分析：区分が切り替わる境目（12と13、64と65）をテストする
def test_12歳は子ども():
    assert get_fee_category(12) == "子ども"

def test_13歳は大人():
    assert get_fee_category(13) == "大人"

def test_64歳は大人():
    assert get_fee_category(64) == "大人"

def test_65歳はシニア():
    assert get_fee_category(65) == "シニア"