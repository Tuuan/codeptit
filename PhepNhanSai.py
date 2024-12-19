while True:
    line = input()
    if line == '-1':
        break
    y, z = line.split()
    print(int(z)//sum([int(c) for c in y]))