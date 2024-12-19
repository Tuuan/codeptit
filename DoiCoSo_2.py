from math import log2
t = int(input())
BASE = '0123456789ABCDEF'
for _ in range(t):
    b = int(input())
    s = input() 
    
    n = int(log2(b))
    while len(s) % n != 0:
        s = '0' + s
    
    res = ''
    while len(s) > 0:
        sum = 0
        for j in range(0, n):
            if s[j] == '1':
                sum += 2 ** abs(j - (n - 1))
        res += BASE[sum]
        s = s[n:]
    
    print(res)