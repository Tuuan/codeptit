n = int(input())
list = []
for i in range(n):
    s = input()
    a = 1
    for j in range(len(s)):
        if s[j] == "(":
            list.append(a) 
            print(a, end = " ")
            a+=1
        elif s[j] == ")":
            print(list.pop(), end =" ")
    if i < n-1:
        print()
