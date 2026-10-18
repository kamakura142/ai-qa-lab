# レッスン4：関数

# Q1：60点以上なら "合格"、それ以外は "不合格" を返す関数
def judge(score):
    if score >= 60:
        return "合格"
    else:
        return "不合格"

assert judge(60) == "合格"      # 境界値：ちょうど
assert judge(59) == "不合格"    # 境界値：1つ下


# Q2：2つの数を受け取って、足した結果を返す関数
def add(a, b):
    return a + b

assert add(2, 3) == 5


# Q3：テスト結果のリストを受け取って、PASSED の数を返す関数（レッスン3の応用）
def count_passed(results):
    count = 0
    for r in results:
        if r == "PASSED":
            count = count + 1
    return count                         # 数えた結果を返す

assert count_passed(["PASSED", "FAILED", "PASSED"]) == 2
assert count_passed([]) == 0     # 境界値：空のリスト


# Q4：会員リストを受け取って、全員の名前のリストを返す関数を「自分で」作る
#     関数名：get_names　引数：members
def get_names(members):
    names = []
    for m in members:
        names.append(m["name"])
    return names

members = [
    {"name": "テスト太郎", "age": 10},
    {"name": "テスト花子", "age": 30},
]
assert get_names(members) == ["テスト太郎", "テスト花子"]

print("レッスン4 すべて正解！")