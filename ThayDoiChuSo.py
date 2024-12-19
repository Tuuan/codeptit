t = int(input())
for _ in range(t):
    list = [int(i) for i in input().split()]
    s1 = list[0]
    s2 = list[1]
    g = input().split()
    if len(g)==1:
        a = g[0]
        b = input()
    else:
        a, b= g
    
    a = a.replace(str(s1),str(s2))
    b = b.replace(str(s1),str(s2))
    sum1 = int(a)+int(b)
    a = a.replace(str(s2),str(s1))
    b = b.replace(str(s2),str(s1))
    sum2 = int(a)+int(b)
    print(min(sum1,sum2),max(sum1,sum2))