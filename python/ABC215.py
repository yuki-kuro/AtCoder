# A - Your First Judge
# 文字列の一致判定
'''
s = input()
h = 'Hello,World!'

# a は長さが一致しているか
a = (len(s) == len(h))
b = True

# 文法修正：range() を追加
# そもそも長さが違う場合に s[i] を参照するとエラーになる可能性があるため、
# a が True のときだけループするようにするとより安全です。
if a:
    for i in range(len(s)):
        if s[i] != h[i]:
            b = False
            break
else:
    b = False

if a and b:
    print('AC')
else:
    print('WA')
'''
# ==で文字列が完全に一致するか判定できる。
s = input()

if (s=="Hello,World!"):
  print("AC")
else:
  print("WA")
