n, m = map(int, input().split())
a = {}
import re
for i in range(n):
    s = input()
    s = s.lower()
    for x in re.findall('\w+', s):
        if x in a:
            a[x] += 1
        else:
            a[x] = 1

a = sorted(a.items(), key = lambda x : (-x[1], x[0]))

for x in a:
    if x[1] >= m:
        print(x[0], x[1])
