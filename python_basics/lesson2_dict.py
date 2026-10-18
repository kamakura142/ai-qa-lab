# レッスン2：辞書

case = {"id": "TC-001", "title": "ログイン成功", "priority": "高"}

# Q1："title" の値を取り出す
q1 = case["title"]
assert q1 == "ログイン成功"

# Q2："id" の値を取り出す
q2 = case["id"]
assert q2 == "TC-001"

# Q3："priority" を "中" に書き換える（「q3 =」なしで書く）
case["priority"] = "中"
assert case["priority"] == "中"

# Q4：見出し "result"、値 "OK" を追加する（「q4 =」なしで書く）
case["result"] = "OK"
assert case["result"] == "OK"

# Q5：見出しの数を数える（レッスン1と同じ道具）
q5 = len(case)
assert q5 == 4


# ---- 応用：リストの中に辞書（test_fixture.py の会員リストと同じ形）----
members = [
    {"name": "テスト太郎", "age": 10},
    {"name": "テスト花子", "age": 30},
]

# Q6：1人目の名前を取り出す（ヒント：まず行番号、次に見出し）
q6 = members[0]["name"]
assert q6 == "テスト太郎"

# Q7：2人目の年齢を取り出す
q7 = members[1]["age"]
assert q7 == 30

print("レッスン2 すべて正解！")