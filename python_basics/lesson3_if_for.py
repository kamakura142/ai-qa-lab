# レッスン3：if文・for文

# ---- if文 ----
# Q1：年齢から区分を決める（get_fee_category と同じ考え方）
age = 70
if age < 13:
    category = "子ども"
elif age < 65:
    category = "大人"
else:
    category = "シニア"
assert category == "シニア"


# ---- for文 ----
# Q2：テスト結果のうち、PASSED の数を数える
results = ["PASSED", "FAILED", "PASSED", "PASSED"]
count = 0
for r in results:
    if r == "PASSED":
        count = count + 1      # count を1増やす
assert count == 3


# ---- for文 × 辞書（レッスン2の応用）----
members = [
    {"name": "テスト太郎", "age": 10},
    {"name": "テスト花子", "age": 30},
    {"name": "テスト次郎", "age": 70},
]

# Q3：全員の名前をリストに集める
names = []
for m in members:              # m には1人分の辞書が入る
    names.append(m["name"])         # その人の名前を追加
assert names == ["テスト太郎", "テスト花子", "テスト次郎"]

# Q4：65歳以上（シニア）の人数を数える
senior = 0
for m in members:
    if m["age"] >= 65:                   # その人の年齢が 65 以上なら
        senior = senior + 1
assert senior == 1

print("レッスン3 すべて正解！")