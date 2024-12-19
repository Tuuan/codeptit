n, k = map(int, input().split())
a1  = [int(x) for x in input().split()]
a2 =  [int(x) for x in input().split()]
a = [[]]*n
for i in range(n):
    a[i] = [a1[i], a2[i]]
a.sort(key=lambda x: x[0]-x[1])
res = 0
for i in range(k):
    res += a[i][0]

for i in range(k, n):
    if a[i][0] - a[i][1] <= 0:
        res += a[i][0]
    else: res += a[i][1]
print(res)

