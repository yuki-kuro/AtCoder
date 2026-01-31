# ABC 049 C - Daydream
'''
s = input()
s = s[::-1]
a,b,c,d = 'dream', 'dreamer', 'erase', 'eraser'
words = [a[::-1],b[::-1],c[::-1],d[::-1]]
i = 0
can2 = True
while i <len(s):
    can = False
    for j in range(4):
        w = words[j]
        if w== s[i:i+len(w)]:
            can =True
            i += len(w)
            break
    if not can :
        can2= False
        break
if can2:
    print('YES')
else:
    print('NO')
'''

# AGC 013 A - Sorted Arrays


















