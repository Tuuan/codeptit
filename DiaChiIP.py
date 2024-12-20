def check(s):
    if len(s) < 4:
        return False
    for i in s:
        if i.isdigit():
            if int(i) > 255 or int(i) < 0:
                return False
        else:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input().split(".")
    if check(s):
        print("YES")
    else:
        print("NO")