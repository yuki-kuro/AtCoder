# ABC 085 B - Kagami Mochi
'''
n=int(input())
d = []
for i in range(n):
    d.append(int(input()))
'''
'''
# バケット法
x=[0]*101
for i in range(n):
    x[d[i]] += 1
ans=0
for i in range(101):
    if x[i] !=0:
        ans+=1 
print(ans)
'''
# setを使った解法
'''
ans = len(set(d))
print(ans)
'''
# dictを使った解法
'''
counts = {}
for x in d:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1
# 辞書のキー（数字の種類）の数が答え
print(len(counts))
'''
# Counterを使う解法
'''
from collections import Counter
# これだけで各要素の出現回数が辞書形式で入る
counts = Counter(d)
print(counts)
print(len(counts))
'''

# ABC 071 B - Not Found
'''
def f(x):
    all='abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        if x==all[i]:
            return i
s=input()
d = [0] *26
all = 'abcdefghijklmnopqrstuvwxyz'
l=[]
for i in range(len(s)):
    l.append(f(s[i]))
l = sorted(l)
ans ="None"
for i in range(26):
    if i not in l:
        ans =all[i]
        break 
print(ans)
'''

# ABC 061 B - Counting Roads
'''
n,m = map(int,input().split())
a = [0] *m
b = [0] *m
for i in range(m):
    a[i],b[i]= map(int,input().split())
dict={}
for x in a:
    if x in dict:
        dict[x] +=1
    else:
        dict[x] = 1
for x in b:
    if x in dict:
        dict[x] +=1
    else:
        dict[x] = 1    
for i in range(1,n+1):
    print(dict[i])
'''

# ABC 047 B - Snuke's Coloring 2 (ABC Edit)
'''
# WAの回答
w,h,n = map(int,input().split())
x =[0]*n
y =[0]*n
a =[0]*n
d=[[0,0],[w,0],[0,h],[w,h]]
for i in range(n):
    x[i], y[i],a[i]=map(int,input().split())
    if a[i] ==1:
        d[0][0]=x[i]
        d[2][0]=x[i]
    if a[i] ==2:
        d[1][0]=x[i]
        d[3][0]=x[i]
    if a[i] ==3:
        d[0][1]=y[i]
        d[1][1]=y[i]
    if a[i] ==4:
        d[2][1]=y[i]
        d[3][1]=y[i]
ans = (d[1][0]-d[0][0])*(d[2][1]-d[0][1])
if ans <0:
    ans=0
print(ans)
'''
'''
w,h,n = map(int,input().split())
lx,rx,dy,uy= 0,w,0,h
# 「1行ずつ処理して答えを更新できる」場合は入力をリストで受け取らなくてよい
for _ in range(n):
    x, y,a=map(int,input().split())
    if a ==1:
        lx = max(lx,x)
    if a ==2:
        rx = min(rx,x)
    if a ==3:
        dy = max(dy,y)
    if a ==4:
        uy = min(uy,y)
# 幅と高さが 0 未満にならないように計算する
width = max(0, rx - lx)
height = max(0, uy - dy)
print(width*height)
'''


# ABC 091 B Two Colors Card Game
'''
# dict を使う
n=int(input())
s=[input()for _ in range(n)]
m=int(input())
t=[input()for _ in range(m)]
ans=0
d={}
for i in range(n):
    if s[i] in d:
        d[s[i]] +=1
    else:
        d[s[i]] = 1
for i in range(m):
    if t[i] in d:
        d[t[i]] -=1
    else:
        d[t[i]] = -1
ans=max(0,max(d.values()))
print(ans)
'''
'''
# Counterを使う
from collections import Counter
n=int(input())
s=[input()for _ in range(n)]
m=int(input())
t=[input()for _ in range(m)]
# 単語の出現回数を一気にカウント
blue_counts = Counter(s)
red_counts = Counter(t)
ans = 0
# 青いカードにある単語を順にチェック
for word in blue_counts:
    score = blue_counts[word] - red_counts[word]
    ans = max(ans, score)
print(ans)
'''
'''
# AC
from collections import Counter
n =int(input())
s = [input() for _ in range(n)]
m =int(input())
t = [input() for _ in range(m)]
cnt_s= Counter(s)
cnt_t= Counter(t)
ans =[]
for k in cnt_s:
    point = cnt_s[k]-cnt_t[k]
    ans.append(point)
print(max(0,max(ans)))
'''

# ABC 081 C - Not so Diverse

from collections import Counter
n,k = map(int,input().split())
a = list(map(int,input().split()))
c = Counter(a)
l = sorted(c.values(), reverse=True)
ans=0
for i in range(k,len(l)):
    ans+=l[i]
print(ans)


