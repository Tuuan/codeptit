tmp = [True] * (10**6+8)
tmp[0] = tmp[1] = False

for i in range(2,1000):
    if(tmp[i]):
        for p in range(i*i,10**6+8,i):
            tmp[p] = False

import math
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(13,n):
        rev = int(str(i)[::-1])
        if tmp[i] and tmp[rev] and rev < n and rev > i:
            print(i, rev, end =" ")
    print()
