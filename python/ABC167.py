# A - Registration

# 文字列の削除
s = input()
t = input()
# スライスを使う
T = t[:len(s)]
T = t[:-1]
if T == s :
    print('Yes')
else:
    print('No')

# startswith()を使う
# TがSで始まり、かつ長さが S+1 であるか
if T.startswith(s) and len(T) == len(s) + 1:
    print('Yes')
else:
    print('No')