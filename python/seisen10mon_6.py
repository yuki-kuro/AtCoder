# ABC 088 B - Card Game for Two
'''
n = int(input())
an = list(map(int,input().split()))
sorted_an = sorted(an,reverse=True)
a=[]
b=[]
for i in range(n):
    if i%2 ==0:
        a.append(sorted_an[i])
    else:
        b.append(sorted_an[i])
print(sum(a)-sum(b))
'''

# ABC 067 B - Snake Toy
'''
n,k = map (int,input().split())
l = list(map (int,input().split()))
sorted_l = sorted(l,reverse=True)
ans = 0
for i in range(k):
    ans += sorted_l[i]
print(ans)
'''

# ABC 042 B - Iroha Loves Strings
'''
n,l =map(int,input().split())
s = [None] *n
for i in range(n):
    s[i] =input()
sorted_s =sorted(s)
print("".join(sorted_s))
'''

# AGC 027 A - Candy Distribution Again
'''
n,x= map(int,input().split())
a = list( map(int,input().split()))
sorted_a = sorted(a)
cnt=0
for i in range(n):
    if x >= sorted_a[i]:
        x = x-sorted_a[i]
        cnt+=1
    else:
        x=0
        break
if x!=0:
    cnt-=1
print(cnt)
'''

# AGC 012 A - AtCoder Group Contest

n = int(input())
a = list(map(int,input().split()))
a = sorted(a,reverse=True)
sum=0
for i in range(1,n*2,2):
    sum += a[i]
print(sum)
