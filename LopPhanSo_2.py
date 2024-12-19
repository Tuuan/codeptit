import math
class PhanSo:
    x, y, x1, y1 = map(int, input().split())
    
    def Tong(self):
        x = self.x * self.y1 + self.x1 * self.y
        y = self.y * self.y1
        gcd = math.gcd(x,y)
        x = x/gcd
        y = y/gcd
        return str(int(x))+"/"+str(int(y))
    
r = PhanSo()
print(r.Tong())