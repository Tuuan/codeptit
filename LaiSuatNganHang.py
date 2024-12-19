for _ in range(int(input())):
    n = [float(i) for i in input().split()]
    money = n[0]
    interest = n[1]
    income = n[2]

    for i in range(1, 1000):
        money = money + money * interest / 100
        if money >= income:
            print(i)
            break