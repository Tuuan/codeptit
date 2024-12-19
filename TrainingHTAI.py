for t in range(int(input())):
    n = int(input())
    u = float(input())
    arr = sorted([float(x) for x in input().split()])

    a = []
    f = {}
    for i in arr:
        if i in f: 
            f[i] += 1
        else:
            f[i] = 1
    for i in f:
        a.append([i, f[i]])
    
    j = 0
    for i in range(len(a) - 1):
        diff = a[i + 1][0] - a[i][0]
        if u >= diff * a[i][1]:
            u -= diff * a[i][1]
            a[i + 1][1] += a[i][1]
            a[i][1] = 0
            j = i + 1
        else:
            break
    
    a[j][0] += u / a[j][1]
    
    res = 1.0
    for i in range(j, len(a)):
        if a[i][1] > 0:
            res *= a[i][0] ** a[i][1]
    
    print(f'{min(1, res):.6f}') 