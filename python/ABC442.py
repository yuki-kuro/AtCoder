# A
# s= input()
# ans =0
# for i in range(len(s)):
#     if(s[i]=="i" or s[i]=="j"):
#         ans+=1
# print(ans)

# B
# q=int(input())
# a=[]
# for i in range(q):
#     a.append(int(input()))
# # for i in range(q):
# #     print(a[i])

# onryo=0
# kyoku = False


# for i in range(q):
#     if(a[i]==1):
#         onryo +=1
#     elif(a[i]==2):
#         if(onryo>=1):
#             onryo-=1
#     elif(a[i]==3):
#         if(kyoku):
#             kyoku=False
#         else:
#             kyoku=True

#     if(onryo>=3 and kyoku == True):
#         print("Yes")
#     else:
#         print("No")


# C
# import math
# n,m = map(int, input().split())
# a=[]
# b=[]
# for i in range(m):
#     aa,bb = map(int, input().split())
#     if(aa<bb):
#         a.append(aa)
#         b.append(bb)
#     else:
#         a.append(bb)
#         b.append(aa)

# x=[]
# for i in range(1,n + 1):
#     cnt=0
#     for j in range(m):
#         if(a[j]==i or b[j]==i):
#             cnt+=1
#     ans=0
#     if(n-1-cnt < 3):
#         ans = 0
#     else:
#         ans = math.comb(n-1-cnt, 3)
#     x.append(ans)
# s=""
# for i in range(n):
#     s = s + str(x[i]) +" "
# print(s)

import math
n,m = map(int, input().split())
a=[]
b=[]
for i in range(m):
    aa,bb = map(int, input().split())
    a.append(aa)
    b.append(bb)

x=[n-1]*n
for i in range(m):
    x[a[i]-1] -=1
    x[b[i]-1] -=1
for i in range(n):
    if(x[i]<3):
        x[i]=0
    else:
        x[i]= math.comb(x[i],3)
print(*x)