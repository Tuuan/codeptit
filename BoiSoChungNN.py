MOD = 10**9 + 7
from math import *

def ds(a):
    list = []
    list.append(a)
    for i in range(1,a):
        if a % i == 0:
            list.append(i)
    count = 0
    for x in list:
        for y in list:
            if (x * y) // gcd(x,y) == a:
                count += 1
                count %= MOD
    return count%MOD
            
t = int(input())
for z in range(t):
    a, b = map(int,(input().split()))
    result = a
    for i in range(a+1,b+1):
        result *= i
    print(ds(result))