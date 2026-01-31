# 文字列練習問題Lv2
# https://shiki-sci.jp/kyopro/string/

'''
# ABC041 - A AC

s = input()
i = int(input())
print(s[i-1])

# ABC218 - A AC

n = int(input())
s = input()
if s[n-1] =='x':
    print('No')
else:
    print('Yes')

# abc244_a  AC

n = int(input())
s = input()
print(s[n-1])

# abc266_a AC

s = input()
print(s[len(s)//2])

# abc038_a AC

s = input()
if s[-1] =='T':
    print('YES')
else:
    print('NO')

# abc179_a AC

s = input()
if s[-1] != 's':
    print(s+'s')
else :
    print(s +'es')

# abc216_a AC

x,y = input().split('.')
y = int(y)
if 0<=y and y <=2:
    print(x+'-')
elif 3 <= y and y <=6:
    print(x)
elif 7 <= y and y <=9:
    print(x+'+')

# abc160_a AC

s = input()
if s[2]==s[3] and s[4] == s[5]:
    print('Yes')
else:
    print('No')

# abc254_a AC

n = input()
print(n[-2:])

# abc236_a AC

s = input()
a,b = map(int,input().split())
# スライスを利用
# print(s[:a-1] + s[b-1] + s[a:b-1]+s[a-1]+s[b:])
# 文字列をリストに変換後、入れ替える(Pythonでは文字列はイミュータブル)
l = list(s)
l[a-1],l[b-1] = l[b-1],l[a-1] # Pythonでは一時変数は不要
print("".join(l))

# abc224_a AC

s = input()
if s.endswith('er'): # スライス s[-2:]
    print('er')
elif s.endswith('ist'): # スライス s[-3:]
    print('ist')

# abc060_a AC

a,b,c  = map(str,input().split())
if a[-1] ==b[0] and b[-1] == c[0]:
    print('YES')
else:
    print('NO')

# abc069_b AC

s = input()
n = len(s)-2
print(s[0]+str(n)+s[-1])

# abc111_a AtCoder Beginner Contest 999 AC

n = input()
# (解法1)forとifで新しい文字列を作成する
ans =[]
for i in range(3):
    if n[i] == '1':
        ans.append('9')
    elif n[i] == '9':
        ans.append('1')
print(''.join(ans))

# (解法2)replace()メソッドを使う
# 1を一旦 'x' に逃がしてから入れ替える
print(n.replace('1', 'x').replace('9', '1').replace('x', '9'))

# (解法3)translate()メソッドを使う。※処理が高速
# 置換テーブル（1を9に、9を1に）を作成して適用
table = str.maketrans('19', '91')
print(n.translate(table))

# abc197_a
s = input()
print(s[1:3]+s[0])

# abc247_a
s = input()
print('0' + s[0:3])

# abc081_a
s = input()
print(s.count('1'))

# abc095_a
s = input()
cnt = s.count('o')
ans = 700 + cnt *100
print(ans)
'''
# abc139_a
s =input()
t =input()
cnt=0
for i in range(len(s)):
    if s[i] ==t[i]:
        cnt+=1
print(cnt)

# abc101_a

s = input()
cnt =0
for i in range(len(s)):
    if s[i] == '+':
        cnt+=1
    if s[i] == '-':
        cnt-=1
print(cnt)










