t = int(input())
for i in range(t):
    list = [int(i) for i in input().split()]
    d = list[0]
    m = list[1]
    if m == 3 and d >=21 or m == 4 and d < 20:
        print("Bach Duong")
    elif m == 4 and d >=20 or m == 5 and d <= 20:
        print("Kim Nguu")
    elif m == 5 and d >=21 or m == 6 and d <= 20:
        print("Song Tu")
    elif m == 6 and d >=21 or m == 7 and d <= 22:
        print("Cu Giai")
    elif m == 7 and d >=23 or m == 8 and d <= 22:
        print("Su Tu")
    elif m == 8 and d >=23 or m == 9 and d <= 22:
        print("Xu Nu")
    elif m == 9 and d >=23 or m == 10 and d <= 22:
        print("Thien Binh")
    elif m == 10 and d >=23 or m == 11 and d <= 22:
        print("Thien Yet")
    elif m == 11 and d >= 23 or m == 12 and d <=21:
        print("Nhan Ma")
    elif m == 12 and d >=22 or m == 1 and d <=19:
        print("Ma Ket")
    elif m == 1 and d >=20 or m == 2 and d <=18:
        print("Bao Binh")
    elif m == 2 and d >=19 or m == 3 and d <=20:
        print("Song Ngu")