# ABC087 B - Coins
'''
a = int(input())
b=int(input())
c=int(input())
x=int(input())
res=0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i*500+j*100+k*50 == x:
                res +=1
print(res)
'''

# ABC105 B - Cakes and Donuts 
'''
n=int(input())
flg = False
for i in range(100):
    for j in range(100):
        if i *4 +j*7 == n:
            flg = True
if flg:
    print('Yes')
else:
    print('No')
'''
# ABC144 B - 81
'''
n = int(input())
flg = False
for i in range(10):
    for j in range(10):
        if i*j==n:
            flg=True
            break
if flg :
    print("Yes")
else:
    print('No')
'''

# ABC133 B - Good Distance
'''
n,d = map(int,input().split())
x=[0] *n
for i in range(n):
    x[i]=list(map(int,input().split()))
cnt=0
for i in range(n):
    for j in range(i+1,n):
        sum=0
        for k in range(d):
            sum += abs(x[i][k] - x[j][k])**2
        for l in range(400):
            if sum == l**2:    
                cnt+=1
print(cnt)
'''

# ABC 175 B - Making Triangle　
'''
n = int(input())
l = list(map(int,input().split()))
cnt=0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if l[i]==l[j] or l[j]==l[k] or l[k]==l[i]:
                continue
            t = [l[i], l[j],l[k]]
            sorted_t = sorted(t)
            if sorted_t[2] < sorted_t[0] + sorted_t[1]:
                cnt+=1
print(cnt)
'''

            
