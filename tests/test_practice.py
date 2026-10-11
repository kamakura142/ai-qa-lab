# pytest ライブラリを読み込む（pytest.raises を使うために必要）
import pytest

# ============================================================
# 練習問題：送料計算（同値分割 + 境界値分析）
# ============================================================
#
# 【仕様】購入金額（円）から送料を返す関数 calculate_shipping_fee
#   -    0円 〜  4,999円 → 送料 500円
#   - 5,000円 〜  9,999円 → 送料 300円
#   - 10,000円以上        → 送料 0円（送料無料）
#   - 0円未満（マイナス） → ValueError（エラーを発生させる）
#
# 【あなたの課題】
#   このファイルの下の方に、テスト関数を自分で書いてください。
#   1. 同値分割：有効・無効の同値クラスを洗い出す（コメントでメモしてOK）
#   2. 境界値分析：各クラスの境目の値を選ぶ
#   3. テストを書いて pytest tests/test_practice.py -v で実行する
#
# 【ヒント】
#   - 同値クラスはいくつありますか？（有効が3つ + 無効が1つ）
#   - 境目の値は「境界の1つ下・ちょうど・1つ上」を意識すると漏れにくいです
#   - 例外（エラー）が出ることの確認は pytest.raises を使います。
#     書き方が分からなければ、調べる前に「こう書きたい」という案を送ってください
# ============================================================


# テスト対象の関数（変更しないこと）
def calculate_shipping_fee(amount):
    # マイナスの金額は不正な入力として扱う
    if amount < 0:
        raise ValueError("金額は0以上で指定してください")

    if amount < 5000:
        return 500
    elif amount < 10000:
        return 300
    else:
        return 0


# ↓↓↓ ここからテストを書いてください ↓↓↓
# 境界値分析：区分が切り替わる境目（0と4999、5000と9999、10000）をテストする
def test_マイナス1円はエラー():
    with pytest.raises(ValueError):
        calculate_shipping_fee(-1)

def test_0は送料500円():
    assert calculate_shipping_fee(0) == 500

def test_4999円は送料500円():
    assert calculate_shipping_fee(4999) == 500

def test_5000円は送料300円():
    assert calculate_shipping_fee(5000) == 300

def test_9999円は送料300円():
    assert calculate_shipping_fee(9999) == 300

def test_10000円は送料無料():
    assert calculate_shipping_fee(10000) == 0
