import re
def solve(lst):
    res = []
    for i in lst:
        if not i.isdigit():
            res.append(i)
        else:
            num = int(i)
            if num >= 2**31 or num < -2**31:
                res.append(i)
    return res
f = open('DATA.in', 'r')
conttent = f.read()
lst = re.findall('\S+', conttent)
res = sorted(solve(lst))
for i in res:
    print(i, end=" ")
f.close()
