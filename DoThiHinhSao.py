n = int(input())
list = {}
for i in range(n-1):
    a,b = map(int, input().split()) 
    if a in list:
        list[a].append(b)
    else:
        list[a] = [b]
    if b in list:
        list[b].append(a)
    else:
        list[b] = [a]
a = 0    
for x in list:
    if len(list[x]) > 1:
        a+=1

if a == 1:
    print("Yes")
else:
    print("No")