# レッスン5：クラス

class Cart:
    def __init__(self, is_member):
        self.is_member = is_member
        self.items = []

    # Q1：商品を入れる（辞書にしてリストに追加）
    def add(self, name, price):
        self.items.append({"name": name, "price": price})

    # Q2：商品の数を返す
    def count(self):
        return len(self.items)

    # Q3：合計金額を返す（レッスン3・4の応用：forで price を足していく）
    def total(self):
        result = 0
        for item in self.items:
            result = result + item["price"]
        return result

    # Q4：送料を返す（会員かつ5000円以上なら0円、それ以外は500円）
    def shipping(self):
        if self.is_member and self.total() >= 5000:   # and ＝「かつ」
            return 0
        else:
            return 500


# ---- 使ってみる ----
# Q5：会員のかごを作る
cart = Cart(True)

cart.add("りんご", 3000)
cart.add("みかん", 2000)

assert cart.count() == 2
assert cart.total() == 5000
assert cart.shipping() == 0         # 境界値：ちょうど5000円の会員


# Q6：一般（非会員）のかごを別に作り、同じ商品を入れたら送料500円になることを確認
other = Cart(False)
other.add("りんご", 3000)
other.add("みかん", 2000)
assert other.shipping() == 500

# かごが別々なので、cart の中身は変わっていない
assert cart.count() == 2

print("レッスン5 すべて正解！")