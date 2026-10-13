import pytest
from shipping import calculate_shipping


# 決定表テスト：会員区分 × 購入金額 → 送料
@pytest.mark.parametrize("is_member, amount, expected", [
    (True, 5000, 0),   # ルール1：会員・5,000円以上
    (True, 4999, 300),   # ルール2：会員・5,000円未満
    (False, 5000, 300),   # ルール3：一般・5,000円以上
    (False, 4999, 500),   # ルール4：一般・5,000円未満
])
def test_送料の決定表(is_member, amount, expected):
    assert calculate_shipping(is_member, amount) == expected