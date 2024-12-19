t = int(input())
for z in range(t):
    n,m =input().split()
    n = int(n)
    m = int(m)
    list = [int(x) for x in input().split()]
    a = []
    for i in range(m):
        a.append(list[i])
    for i in range(m,n):
        print(list[i],end=" ")
    for i in a:
        print(i, end=" ")
    if(z < t-1):
        print()