class Matrix:
    def __init__(self, n, m, mt):
        self.n = n
        self.m = m
        self.mt = mt
        
    def __mul__(self):
        res = []
        for i in range(self.n):
            res += [[0]*self.n]
            for j in range(self.n):
                for z in range(self.m):
                    res[i][j] += self.mt[i][z]*self.mt[j][z]
        return res
    

t = int(input())
for _ in range(t):
    n, m = [int(i) for i in input().split()]
    mt = []
    for i in range(n):
        mt.append([int(j) for j in input().split()])
    a = Matrix(n, m, mt)
    for i in a.__mul__():
        for j in i:
            print(j, end=" ")
        print()