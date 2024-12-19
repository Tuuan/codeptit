import math
t = int(input())
def SNT(n):
    a = 0
    if n == 0 or n == 1:
        return 0
    for i in range(2,n):
        if(n%i==0):
            a = 1
            return 0
    if a == 0:
        return 1
for i in range(t):
    n = int(input())
    count = 0
    for j in range(n):
         if math.gcd(j,n) == 1:
             count += 1
    if SNT(count):
        print("YES")
    else:
        print("NO")
