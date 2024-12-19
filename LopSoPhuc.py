import math as m
class SoPhuc:
    def __init__(self, a, b, a1, b1):
        self.a = a
        self.b = b
        self.a1 = a1
        self.b1 = b1
    def mul (self):
        a = self.a+self.a1
        b = self.b+self.b1
        
        x = a*self.a - b*self.b
        y = a*self.b + b*self.a
        
        x1 = a**2 - b**2
        y1 = a*b + b*a
        
        if y < 0 and y1 < 0:
            return str(int(x)) +" - "+ str(int(m.fabs(y))) + "i, "+str(int(x1)) + " - " + str(int(m.fabs(y1)))+"i"
        elif y < 0:
            return str(int(x)) +" - "+ str(int(m.fabs(y))) + "i, "+str(int(x1)) + " + " + str(int(m.fabs(y1)))+"i"
        elif y1 < 0:
            return str(int(x)) +" + "+ str(int(m.fabs(y))) + "i, "+str(int(x1)) + " - " + str(int(m.fabs(y1)))+"i"
        else:
            return str(int(x)) +" + "+ str(int(m.fabs(y))) + "i, "+str(int(x1)) + " + " + str(int(m.fabs(y1)))+"i"
        
for _ in range(int(input())):
    a,b,c,d = map(int, input().split())
    v = SoPhuc(a,b,c,d)
    print(v.mul())
            