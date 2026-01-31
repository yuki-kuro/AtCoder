# EX11 - 足したり引いたり
'''
s=input()
ans = 1
for i in range(1,len(s),2):
    if(s[i] =='+'):
        ans += 1
    else:
        ans-=1
print(ans)
'''

# EX12 - 最速のランナーを見つけよう
'''x
n = int(input())
t = list(map(int, input().split()))
min = min(t)
for i ,v in enumerate(t):
    if min == v:
        print(i+1)
# for i in range(n):
#     if(min==t[i]):
#         print(i+1)
'''

# EX13 - 三人兄弟へのプレゼント
'''
def sum_scores(scores):
    """
    1 人のテストの点数を表すリストから合計点を計算して返す関数

    引数 scores: scores[i] に i 番目のテストの点数が入っている
    返り値: 1 人のテストの合計点
    """
    # ここにプログラムを追記
    # total = 0
    # for s in scores:
    #     total += s
    # return total

    s = sum(scores)
    return s


def output(sum_a, sum_b, sum_c):
    """
    3 人の合計点からプレゼントの予算を計算して出力する関数

    引数 sum_a: A 君のテストの合計点
    引数 sum_b: B 君のテストの合計点
    引数 sum_c: C 君のテストの合計点
    返り値: なし
    """
    # ここにプログラムを追記
    print(sum_a * sum_b * sum_c)
    return


# -------------------
# ここから先は変更しない
# -------------------


def input_list(N):
    """
    N 個の入力を受け取ってリストに入れて返す関数

    引数 N: 入力を受け取る個数
    返り値: 受け取った N 個の整数値からなるリスト
    """
    l = list(map(int, input().split()))
    return l


# 科目の数 N を受け取る
N = int(input())

# それぞれのテストの点数を受け取る
A = input_list(N)
B = input_list(N)
C = input_list(N)

# それぞれの合計点を計算
sum_A = sum_scores(A)
sum_B = sum_scores(B)
sum_C = sum_scores(C)

# プレゼントの予算を出力
output(sum_A, sum_B, sum_C)
'''

# EX14 - 隣り合う同じ値を探す
'''
data = [int(c) for c in input().split()]
flg= False
for i in range(4):
    if data[i] == data[i+1]:
        flg = True

if flg:
    print("YES")
else:
    print("NO")
'''
# EX15 - 果物屋さんでお買い物

n,s = map(int,input().split())
a = list(map(int,input().split()))
p = list(map(int,input().split()))
cnt=0
# for i in range(n):
#     for j in range(n):
#         if a[i] +p[j] == s:
#             cnt+=1
for x in a:
    for y in p:
        if x + y == s:
            cnt += 1
print(cnt)