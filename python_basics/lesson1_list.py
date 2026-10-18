# レッスン1：リスト
# 実行して「すべて正解！」と出ればOK。違うと AssertionError が出ます

cases = ["正常系", "異常系", "境界値"]

# Q1：1番目の要素を取り出す
q1 = cases[0]
assert q1 == "正常系"

# Q2：要素の数を数える
q2 = len(cases)
assert q2 == 3

# Q3："回帰" を最後に追加する（この行は「q3 =」なしで書く）
cases.append("回帰")
assert cases == ["正常系", "異常系", "境界値", "回帰"]

# Q4：最後の要素を取り出す（ヒント：マイナス）
q4 = cases[-1]
assert q4 == "回帰"

# Q5：2番目の要素を取り出す
q5 = cases[1]
assert q5 == "異常系"

print("レッスン1 すべて正解！")