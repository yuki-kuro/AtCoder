#A
'''
n = input()
if(int(n[0])==int(n[1]) and int(n[0])==int(n[2])):
    print("Yes")
else:
    print("No")
'''
#B
'''
n ,k = map(int, input().split())
def digit_sum(x):
    # ベースケース : n が 1 桁ならば、各桁の和は n である
    if x <= 9:
        return x
 
    # n を 1 の位とそれより上の位に分ける
    ones = x % 10    # 1 の位は、n を 10 で割った余りで得られる
    other = x // 10  # 1 の位を取り除いて左に詰めることは、10 で割って切り捨てることに相当する
 
    # 再帰呼び出し : 1 より上の位の各桁の和を求める
    s = digit_sum(other)
 
    # 答えの計算 : 各桁の和を計算
    return s + ones
    
count=0
for i in range(1,n+1):
    if(digit_sum(i) == k): 
        count+=1
print(count)
'''
#C
n= int(input())
a = list(map(int, input().split()))

a2 = sorted(a)
ans=[]
l = a2[n-1]+a2[0]
b=[]
for i in range(n//2):
    b.append(a2[i] +a2[n-1-i])
if(all(val == b[0] for val in b)):
    ans.append(l)


l = a2[n-1]
c=[]
for i in range(a2.count(l)):
    a2.pop()
for i in range(len(a2)//2):
    c.append(a2[i] +a2[len(a2)-1-i])
if(all(val == c[0] for val in c)):
    ans.append(l)

ans2 = sorted(ans)

print(*ans2)




#D