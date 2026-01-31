# A - Handmaid
'''
s = input()
s = s.lower()
print("Of" + s)
'''
# B - Greedy Draft
'''
n,m = map(int,input().split())
l = [0]*n
x = [None]*n
for i in range(n):
    l[i] = int(input())
    x[i] = list(map(int,input().split()))
kan = [0]*m
for i in range(n):
    for j in range(l[i]):
        if kan[x[i][j]-1] == 0:
            kan[x[i][j]-1] += 1
            print(x[i][j])
            break    
    else:
        print(0)
'''            

# C - Omelette Restaurant
'''
# 2026/2/21 実行時間経過
def f(l,x):
    for i in range(len(l)):
        if l[i] >= x:
            l[i] -=x
            x = 0
            return l
        else:
            l[i] = 0
            x = x-l[i]
    return l


t = int(input())
case=[None]*t
n =[0] *t
d = [0] *t
a = []
b = [] 
for i in range(t):
    n[i], d[i] =map(int,input().split())
    a.append(list(map(int,input().split())))
    b.append(list(map(int,input().split())))

for i in range(t):
    tmg = [0]*n[i]   
    for j in range(n[i]):
        tmg[j] += a[i][j]
        tmg = f(tmg, b[i][j])
        if j - d[i] >=0:
            tmg[j - d[i]] = 0
    print(sum(tmg))
''' 

'''
先入先出なのでリストではなくキューを使うと計算量を減らせる。
リストで先頭を削除すると、「添え字を前にずらす」操作が入るため、
計算量が多くかかる
''' 
from collections import deque
t= int(input())
for _ in range(t):
    n,d = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    # 在庫を管理するキュー（中身は「仕入れられた日」の記録）
    q = deque()
    for i in range(n):
        # --- ステップ1: 朝の仕入れ ---
        # i日目に仕入れたa[i]個の卵を在庫(q)に追加する
        for _ in range(a[i]):
            q.append(i)
        # --- ステップ2: 昼の消費 ---
        # 仕入れた順にb[i]個使う（先入れ先出しなので popleft）
        for _ in range(b[i]):
            q.popleft()
        # --- ステップ3: 夜の処分 ---
        # 「仕入れ日(q[0])」が「今日(i)からd日以上前」の卵をすべて捨てる
        # 例: d=2 で今日が i=3 の場合、3-2=1日目以前の卵は処分対象
        # 「qが空でない」という条件をつけないと、q[0]で実行時エラー
        while q and q[0] <= i-d:
            q.popleft()
    # すべての営業日終了後に残っている在庫数を出力
    print(len(q))




# D - Max Straight