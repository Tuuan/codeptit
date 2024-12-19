import math
def nt(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    if a < 2: return False
    return True 
arr = []
sum = 0
n, a = int(input()), list(map(int, input().split()))
for i in a:
    if arr.count(i) == 0:
        arr.append(i)
        sum += i
check = 0
s = 0
for i in range(len(arr)):
    s += arr[i]
    if nt(s) and nt(sum - s):
        print(i)
        check  = 1
        break
if check == 0: print('NOT FOUND')
