import math
m = int(input())
v = int(input())
t = int(input())
d = input()

s = v*t
res = s
if s > m:
    while s > m:
        s -= m
else:
    s = m - s

if d == "C":
    print(f"Result = {int(math.fabs(s))}")
else:
    if res > m:
        while res > m:
            res -= m
    print(f"Result = {res}")
    

