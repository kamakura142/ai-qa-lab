import pytest

# 年齢から料金区分を返す関数（テスト対象）
def get_fee_category(age):
    if age < 13:
        return "子ども"
    elif age < 65:
        return "大人"
    else:
        return "シニア"


# 境界値分析：区分が切り替わる境目（12と13、64と65）をテストする
@pytest.mark.parametrize("age, expected", [
	(12, "子ども"), #子供となる最後の年齢
	(13, "大人"), #大人になる最初の年齢
	(64, "大人"), #大人になる最後の年齢
	(65, "シニア"),
])

def test_子供大人シニア判別(age, expected):
	assert get_fee_category(age) == expected