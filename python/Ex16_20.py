# EX16 - 英単語テスト対策
'''
n,k =map(int, input().split())
s = list(input().split())

ans = [i for i in s if len(i) >= k]
print(*ans)
'''
# EX17 - ゲーム大会
'''
N, M = map(int, input().split())

AB = [list(map(int, input().split())) for i in range(M)]

result = [["-"] * N for _ in range(N)]

for row in AB:
    a = row[0]
    b = row[1]
    
    a -=1
    b -=1
    result[a][b] = "o"
    result[b][a] = "x"

for row in result:
    print(*row)  
    '''

# EX18 - 報告書の枚数
'''
# x 番の組織が親組織に提出する報告書の枚数を返す関数
def num_report(children, x):
    # ここに追記して再帰関数を実装する
        # ベースケース
    if not children[x]:
        return 1
    # 再帰ステップ
    ans = 1 # 自身の報告書
    for c in children[x]:
        ans += num_report(children, c)
    return ans

# これ以降の行は変更しなくてよい
N = int(input())
# p[i] : 組織 i の親組織
# 組織 0 の親組織は存在しないので -1 を入れておく
# 組織 0 に相当する部分は入力で与えられないため、リスト [-1] を作成して "+" 演算子で結合する
p = [-1] + [int(c) for c in input().split()] 

# children[i] = 組織 i の子組織のリスト
children = [[] for _ in range(N)]
for i in range(1, N):
    parent = p[i] # 組織 i の親組織は parent
    children[parent].append(i) # parent の子組織リストに i を追加

# 各組織について答えを計算し出力する
for i in range(N):
    res = num_report(children, i)
    print(res)
'''

# EX20 - 最頻値

'''
# WA
from collections import Counter
n = int(input())
a = list(map(int,input().split()))
cnt_a = Counter(a)
print(cnt_a[max(cnt_a.values())],max(cnt_a.values()))
'''

from collections import Counter
n = int(input())
a = list(map(int, input().split()))
cnt_a = Counter(a)

max_k =0 
max_v =0
for x in cnt_a:
    if max_v < cnt_a[x]:
        max_v = cnt_a[x]
        max_k = x
print(max_k,max_v)