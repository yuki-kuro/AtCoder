#A
# n = int(input())
# print(2**n-2*n)

#B - Happy Number
def f(n):
    res = 0
    for char in str(n):
        digit = int(char)
        res += digit **2
    return res

def main():
    line = input()
    if not line:
        return
    n = int(line)

    history = set()
    while n >1:
        if n in history:
            print("No")
            return
        history.add(n)
        n= f(n)
    print("Yes")
if __name__ == "__main__":
    main()