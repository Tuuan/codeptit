import math

def check(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2,n):
        if n % i == 0:
            return 0
    return 1
for _ in range(int(input())):
    n, m = map(int, input().split())
    gcd = math.gcd(n,m)
    sum = 0
    while gcd>0:
        sum += gcd%10
        gcd //= 10
    if check(int(sum)):
        print("YES")
    else: print("NO")
    