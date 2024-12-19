n = int(input())
a = []
while len(a) < n:
    for i in list(map(int, input().split())):
        a.append(i)
        
a.sort()
check = 1
for i in range(1, a[-1]):
    if a.count(i)==0:
        check = 0
        print(i)

if check == 1: print("Excellent!")