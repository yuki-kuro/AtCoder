# Ex6
# A, op, B = input().split()
# A = int(A)
# B = int(B)

# if op == "+":
#     print(A + B)

# if op == "-":
#     print(A - B)

# if op == "*":
#     print(A * B)

# if op == "/":
#     if(B == 0):
#         print("error")
#     else:
#         print(A // B)

# if (op == "?" or op == "=" or op == "!"):
#     print("error")

# Ex7
# a =  True # True または False
# b =  False # True または False
# c =  True # True または False

# # ここから先は変更しないこと

# assert (a is True) or (a is False)
# assert (b is True) or (b is False)
# assert (c is True) or (c is False)

# if a:
#     print("At", end="")
# else:
#     print("Yo", end="")

# if not a and b:
#     print("Bo", end="")
# else:
#     print("Co", end="")

# if a and b and c:
#     print("foo!", end="")
# elif True and False:
#     print("year!", end="")
# elif not a or c:
#     print("der", end="")

# print("")

# Ex8
# n = int(input())
# for i in range(n):
#   a,b = map(int,input().split())
#   print(a+b)

# EX9 - 電卓をつくろう2
'''
n = int(input())
a = int(input())
s = a
for i in range(n):
    op, b =input().split()
    b = int(b)

    if(op =='+'):
        s += b
    if(op =='-'):
        s -= b
    if(op =='*'):
        s *= b        
    if(op =='/'):
        if(b ==0):
            print('error')
            break
        else:
            s //= b
    print(i+1 ,'',s)
'''

# EX10 - 平均との差
n =int(input())
a =list(map(int, input().split()))
s = 0
for i in a:
    s += i  # sum()を使う
avg = s//n
for i in a:
    if (i - avg >0):
        print(i - avg)  #abs()を使う
    else:
        print(avg - i)

# リスト内包表記で計算結果のリストを作成
# diffs = [abs(i - avg) for i in a]
# 改行して出力
# print(*diffs, sep='\n')
