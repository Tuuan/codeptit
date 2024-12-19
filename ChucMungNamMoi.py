t = int(input())
list = []
for i in range(t):
    s = input()
    if list == []:
        list.append(s)
    elif s not in list:
        list.append(s)
print(len(list))