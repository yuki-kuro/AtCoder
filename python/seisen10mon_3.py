# ABC081 B - Shift only
'''
n = int(input())
a = list(map(int,input().split()))
flg = True
count=0
while(flg):
    for x in a:
        if x % 2==1:
            flg=False
            break
    a = [x//2 for x in a]
    count += 1
print(count-1)
'''
# ABC068 B - Break Number
'''
n = int(input())
ans = 0
res=0
for i in range(1,n+1):
    count=0
    flg=True
    t=i
    while flg:
        if t%2 ==0:
            count+=1
            t=t//2
        else:
            flg = False
    if ans <count :
        ans = count
        res = i
print(res)
'''
'''
def calc(x):
    cnt=0
    while x%2 ==0:
        cnt+=1
        x /=2
    return cnt
n = int(input())
max=-1
ans = 0
for i in range(1,n+1):
    c = calc(i)
    if max < c:
        max = c
        ans = i
print(ans)
'''

# ABC102  B - Maximum Difference
'''
n = int(input())
a = list(map(int,input().split()))
print(max(a) - min(a))
# sorted_a = sorted(a)
# res = sorted_a[n-1]-sorted_a[0]
# print(res)
'''

# ABC113 B - Palace
'''
n =int(input())
t,a =map(int,input().split())
h = list(map(int,input().split()))
res = 0
min_dif = 10**5
for i in range(n):
    avg = t - 0.006*h[i]
    dif = abs(avg-a)
    if min_dif > dif:
        min_dif = dif
        res = i+1
print(res)
'''
# ABC072 B - OddString
'''
s = input()
res =""
for i in range(0,len(s),2):
    res += s[i]
print(res)
'''

# ABC053 B - A to Z String
'''
s = input()
min = -1
max = -1
for i,v in enumerate(s):
    if v=='A':
        if min == -1:
            min = i
    if v=='Z':
        max = i
res = max-min +1
print(res)
'''
# ABC095 B - Bitter Alchemy

n,x = map(int,input().split())
m = []
for i in range(n):
    m.append(int(input()))
res = n
nokori = x-sum(m)
min = min(m)
res += nokori//min
print(res)