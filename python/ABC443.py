# A
# s = input()
# print(s+"s")

# B
# n ,k = map(int, input().split())

# i = 0
# s = n
# if n >= k:
#     print(0)
# else:
#     while s < k:
#         i +=1
#         s += i + n
       
#     print(i)

# C
n ,t = map(int, input().split())
a = list(map(int, input().split()))

# cnt = 0
# X=[]
# a[0]+100*x
# cnt += 100
# print(t-cnt)

total = 0
open = 0
for i in range(n):
    if open < a[i]:
        total += a[i] - open
        open =a[i] +100
if open < t:
    total += t-open
print(total)