import pytest


# 前提条件：会員が3人登録されている
@pytest.fixture
def members():
    return [
        {"name": "テスト太郎", "age": 10},
        {"name": "テスト花子", "age": 30},
        {"name": "テスト次郎", "age": 70},
    ]


# テスト1：会員は3人
def test_会員は3人(members):
    assert len(members) == 3


# テスト2：最初の会員の名前は「テスト太郎」
# ヒント：リストの1番目は [0]、辞書の値は ["name"] で取り出す
def test_最初の会員はテスト太郎(members):
    assert members[0]["name"] == "テスト太郎"


# テスト3：会員を1人追加すると4人になる
def test_会員を追加すると4人(members):
    members.append({"name": "テスト三郎", "age": 40})   # append＝リストの最後に追加
    assert len(members) == 4


# テスト4：テスト3で追加しても、ここでは3人のまま（独立性の確認）
def test_追加の影響を受けない(members):
    assert len(members) == 3