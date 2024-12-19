k = [1]*10
for i in range(2,10):
    k[i] = k[i-1]*i
    
for _ in range(int(input())):
    n = input()
    s = sum(k[int(i)] for i in n)
    print("Yes" if int(n) == s else "No")