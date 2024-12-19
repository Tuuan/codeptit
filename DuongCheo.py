n = int(input())
list = []
while n > 0:
    for i in list:
        print(i, end = ' ')
    for j in range(n):
        print(j, end = ' ')
    print()
    list.append(n-1)
    list.sort()
    n-=1