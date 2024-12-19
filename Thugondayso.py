n = int(input())
list = [int(i) for i in input().split()]
s = []
for i in range(n):
    if s and (s[-1]+list[i])%2==0:
        s.pop()
    else:
        s.append(list[i])
        
print(len(s))