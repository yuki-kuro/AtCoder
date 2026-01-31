# ABC 085 C - Otoshidama
'''
n,Y = map(int,input().split())
for i in range(n+1):
    for j in range(n+1):
        x = i
        y = j
        z = n - x - y
        if z >=0:
            t =x*10000 + y*5000 + z*1000
            if t== Y:
                print(x,y,z)
                # 答えが見つかったら強制終了
                exit()
print(-1,-1,-1)
'''

# ABC 088 C - Takahashi's Information
'''
# 判定条件が不足
c= [list(map(int,input().split())) for _ in range(3)]
ans=False
for i in range(2):
    for j in range(1):
        if c[i][j]-c[i][j+1]==c[i][j+1]-c[i][j+2]:
            ans=True
if ans:
    print('Yes')
else:
    print('No')
'''
'''
c= [list(map(int,input().split())) for _ in range(3)]
x1 = c[0][0] -c[0][1] ==c[1][0]-c[1][1] ==c[2][0]-c[2][1]
x2 = c[0][1] -c[0][2] ==c[1][1]-c[1][2] ==c[2][1]-c[2][2]
y1 = c[0][0] -c[1][0] ==c[0][1]-c[1][1] ==c[0][2]-c[1][2]
y2=  c[1][0] -c[2][0] ==c[1][1]-c[2][1] ==c[1][2]-c[2][2]
if x1 and x2 and y1 and y2 :
    print('Yes')
else:
    print('No')
'''

# ARC 096 C - Half and Half
'''
# 間違い
a,b,c,x,y = map(int,input().split())
if x>=y:
    ab = c*(y)*2 +(x-y)*a
    n_ab = x*a+y*b
else:
    ab = c*(x)*2 +(y-x)*b
    n_ab = x*a+y*b
print(min(ab,n_ab))
'''
'''
a,b,c,x,y = map(int,input().split())
# 十分に大きな値で初期化する
min =float('inf')
for i in range(0,2*10**5+1,2):
    # ピザ枚数がマイナスになるのを防ぐため、max()を使う
    t = i*c +(max(0,x-i//2))*a+(max(0,y-i//2))*b
    if min > t:
        min = t
print(min)
'''

# ABC 057 C - Digits in Multiplication
'''
import math
n= int(input())
# 十分大きな数
min=10**18
for a in range(1,int(math.sqrt(n))+1):
    # 「nがaで割り切れる場合」という条件が必要
    if n % a == 0:
        b = n//a
        tmp= max(len(str(a)),len(str(b)))
        if min > tmp:
            min = tmp
print(min)
'''

# ABC 112 C - Pyramid







