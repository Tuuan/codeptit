n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
m, s, ans, x = {}, 0, 0, 0
for i in a :
    if i in m :
        m[i] += 1
    else :
        m[i] = 1
    s = max(s, m[i])
for i in range(1, k + 1) :
    if i in m and m[i] > x and m[i] != s :
        x = m[i]
        ans = i
if ans == 0 :
    print("NONE")
else :
    print(ans)


