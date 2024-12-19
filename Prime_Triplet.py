import math
tmp = [True]*(10**6+8)
tmp[0] = tmp[1] = False
for i in range(2,math.isqrt(10**6+8)):
    if(tmp[i]):
        for p in range(i*i, 10**6+8,i):
            tmp[p] = False
            
n = int(input())
for _ in range(n):
    m = int(input())
    
    sum = 0
    for i in range(6,m):
        if(tmp[i] and tmp[i-6] and (tmp[i-2] or tmp[i-4])):
            sum+=1
    print(sum)