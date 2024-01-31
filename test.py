# 命令は上から順番
print("Hello world")
print(123)

# 変数
say_hi = "Hi!!"
foo = 123
foo2 = True 

print(type(say_hi))
print(type(foo))
print(type(foo2))

# 条件分岐　if文 (ネストにすることがかなり重要)
size = "m_size"
if size == "s_size":
    print("your_size")
elif size == "m_size":
    print("your_size")
else:
    print("not_your_size")

# 関数
def test_def(arg):
    status = arg

    if status > 2:
        return "over"
    else:
        return "in"

print(test_def(1))


# 配列
test_array = [1, 2, 3, 4, 5]
print(test_array[4])
print(test_array[0:2]) # 0~2番目まで取得
print(test_array[3:]) # 3番目から最後まで取得
print(len(test_array)) # 配列のlength

# for文
for index in range(5):
    print(test_def(index))

# for文 & 配列
for item in test_array:
    if item == 2:
        continue
    if item == 4:
        break
    print(item)

# with構文　open(ファイル名、モード(w, r ))
with open('./test.txt', "r") as file:
    print(file.read())
    print(file.name)


# クラス　インスタンス クラス名は大文字スタート
class Card:
    def __init__(self, date, user_name):
        self.date = date
        self.user_name = user_name
    def message(self):
        return 'この投稿は' + self.user_name + 'さんが' + self.date + 'に投稿しました。'

date_a = "2020-01-01"
user_name_a = "Taro"
card_a = Card(date_a, user_name_a)

print(card_a.user_name)
print(card_a.message())

date_b = "2020-01-01"
user_name_b = "Kayoko"
card_b = Card(date_b, user_name_b)

print(card_b.user_name)
print(card_b.message())
    

# import構文　モジュール
# デフォルトモジュール(pythonが元々持っているもの)
import math
print(math.pi)

import datetime
print(datetime.datetime.today())

# 外部モジュール (pypi: python package index)
# https://pypi.org/
# URLからパッケージを探し、$ pip install {パッケージ名}　でインストー

# 辞書型(オブジェクト)
person = {
    'name': 'Miki',
    'age': 20
}
print(person['age'])

# Array型　+ Dictionary型
accounts = [
    {
        'name': 'Mai',
        'age': 22
    },
    {
        'name': "Yuki",
        'age': 33
    }
]

print(accounts[0]['age'])
