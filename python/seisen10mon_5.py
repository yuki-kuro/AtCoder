# ABC 083 B - Some Sums
'''
def f(x):
    total=0
    while x>0:
        p = x % 10 
        x = x//10
        total += p
    return total

n,a,b = map(int,input().split())
res=0
for i in range(1,n+1):
    if a<=f(i) and f(i)<=b:
        res+= i
print(res)
'''

# ABC 090 B - Palindromic Numbers
'''
def f(x):
    y=[]
    while x>0:
        y.append(x % 10)
        x = x//10
    return y
a,b = map(int,input().split())
cnt=0
for i in range(a,b+1):
    y = f(i)
    if y[0] == y[4] and y[1] == y[3]:
        cnt+=1
print(cnt)
'''
'''
a, b = map(int, input().split())
cnt = 0
for i in range(a, b + 1):
    s = str(i)
    # 文字列を反転させたものと一致するか確認
    if s == s[::-1]:
        cnt += 1
print(cnt)
'''

# AGC 025 A - Digits Sum
'''
def f(x):
    total=0
    while(x>0):
        p = x % 10
        x = x//10
        total +=p
    return total

n = int(input())
min=10**5
for i in range(1,n):
    a = i
    b= n-i
    sum = f(a)+f(b)
    if min > sum:
        min=sum
print(min)
'''

# ABC 156 B - Digits
'''
n,k = map (int,input().split())
cnt =0
while(n>0):
    n = n//k
    cnt+=1
print(cnt)
'''


