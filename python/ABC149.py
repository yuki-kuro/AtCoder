# C - Next Prime
# 素数判定
'''
def f(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

x = int(input())
i=x
while i >=x:
    if f(i):
        print(i)
        break
    i+=1
'''

'''
改善後のコード
1. 計算量 O(x) → O(√x)で劇的に早くなる
2. 例外処理 x=1、x=2の場合
3. 偶数の素数はx=2のみなので、奇数だけを判定することで計算量を減らせる
'''
import math

def is_prime(x):
    # 2.例外処理
    if x < 2: 
        return False
    if x == 2: 
        return True
    if x % 2 == 0: 
        return False
    
    # 3.3から√xまで、奇数だけを確認する
    # 1.O(√x) で判定可能
    for i in range(3, int(math.sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

x = int(input())
i = x
while True:
    if is_prime(i):
        print(i)
        break
    i += 1