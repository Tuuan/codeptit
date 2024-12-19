n= int(input())
a = {}
import re
for i in range(n):
    s = input()
    s = s.lower()
    s = re.findall('\w+', s)
    d = re.findall('\D+', s)
    print(d)
    for x in d:
        if x in a:
            a[x] += 1
        else:
            a[x] = 1

a = sorted(a.items(), key = lambda x : (-x[1], x[0]))

for x in a:
    print(x[0], x[1])
