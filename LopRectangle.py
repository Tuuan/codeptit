class Rectangle:
    def __init__(self, l, w, c):
        self.l = l
        self.w = w
        self.c = c[0:1].upper()+c[1:].lower()
    def perimeter(self):
        p = (self.l + self.w) * 2
        return p
    def area(self):
        a = self.l * self.w
        return a
    def color(self):
        return self.c

if __name__ == '__main__':
    arr = input().split()
    if int(arr[0]) <= 0 and int(arr[1])<=0:
        print("INVALID")
    else:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print(r.perimeter(), r.area(), r.color(),sep = ' ')