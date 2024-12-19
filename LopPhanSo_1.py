import math
class PhanSo:
    x, y = map(int, input().split())
    
    def RutGon(self):
        gcd = math.gcd(self.x, self.y)
        x = self.x/gcd
        y =self.y/gcd
        return str(int(x))+"/"+str(int(y))

r = PhanSo()
print(r.RutGon())