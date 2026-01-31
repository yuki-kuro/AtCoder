# A - Strong Word
'''
s = input()
if(s[0]==s[-1]):
    print("Yes")
else:
    print("No")
'''
# B - Center Alignment
'''
n = int(input())
s =[input() for i in range(n)]

# m=len(s[0])
# for i in range(n-1):
#     if(len(s[i]) <= len(s[i+1])): # 隣同士を比較しているので最大値を取得できていない
#         m = len(s[i+1])
slen = [len(s[i]) for i in range(n)]
m = max(slen)  # max(len(s[i]) for i in range(n))と書ける

for i in range(n):
    k = (m-len(s[i]))//2
    dot =""
    for j in range(k):
        dot = dot +"."  #「文字列の掛け算」を利用する。"." * k
    ans = dot + s[i] + dot
    print(ans)
'''
# C - Sugoroku Destination

n = int(input())
a = list(map(int, input().split()))

def f(x):
    if(x==a[x-1]):
        return x
    x = a[x-1]
    return f(x)

ans = [f(s) for s in range(1,n+1)]
print(*ans)