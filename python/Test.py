#
'''
s = 'JNPGCZBUXHJAVWXGWIZAXTIQYMRRSSYDNUWCJYVZVZZCYZYKWUMOJNZYUJIKCWXUVDDNOYJDXYIXADXJYZNZTSNQDXGUBYSZPRCRPQYIPTXCSIHNZXWFWSQKVYOHWIZJYWZDQSLPIFXRYWYLXWWYDCBWIKJQGWSUXPHCORZXSXLWWOIZPIMQXCWVCMAYWKKPRNWAYYATXCHQCZKTIWIRLOZVQWKXZGYRZUQJXDJQQYMYLNBZXWWMJXPZXKYPGWRETBPPDHUMQMKNUYHFGQKHMYKJKWYTIBZSTOZFHLQVYXLGCNIEXQFAGBWAFMXSWXTCWZKXSAXUZFLUYPWIGKWYUDTOOYYWZYQZXDVJSYSTGJWXNZGZOZSZCXCHZERWCIWYTIPQRWXZWCYYQYUWTNGZXZUBYKYVZWPEKOYZNWKYGPOYXLTWYYTAFYXPXXQWCWSZLMXRGKVCCWLANWWCBZYWLIRYGJRHMKWVBWXWGRLETQNZHYAQUTZK'

s = s.replace('W','')
# s = 'XabXdeaaaaaa'
for i in range(len(s)-3):
    if s[i] == 'X' and s[i+3] != 'X':
        s = s[:i+3] + 'E' + s[i+4:]
# s = 'YZYZadgadsY'
print(len(s))
if 'YZ' in s:
    print('Yes')
else:
    print('No')
s = s.replace('YZ','E')
if 'YZ' in s:
    print('Yes')
else:
    print('No')
print(len(s))
print(s)
for i in range(226, 233):
    print(s[i])
'''

'''
x = 77777
total=0

for n in range(1,3001):
    total +=x%n +x//n
print(total)
'''
'''
import math
def f(x):
    return int(math.sqrt(x))
total =0
n=10**5
ans = 0
for i in range(1,n+1):
    total += f(i)
    if total >=5555555:
        ans = i
        break    

print(total)
print(ans)
'''
s=''
for n in range(1,101):
    t = n%3
    if t ==0 :
        s+='ZERO'*n
    if t ==1 :
        s+='ONE'*n
    if t ==2 :
        s+='TWO'*n
print(s)
print(len(s))
