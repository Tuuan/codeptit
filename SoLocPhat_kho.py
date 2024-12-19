import sys

def precompute():
    precomputed = [0] * 100
    for num in range(8, 8001, 8):
        precomputed[num // 8 % 100] = str(num).count('6') + str(num).count('8')
    return precomputed

precomputed = precompute()

def count68(N):
    if N < 8:
        return 0
    limit = N // 8
    full_cycles = limit // 100
    remainder = limit % 100
    
    count = full_cycles * sum(precomputed) + sum(precomputed[:remainder + 1])
    return count

def solve():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    result = []
    
    for i in range(1, T + 1):
        N = int(data[i])
        result.append(str(count68(N)))
    
    print("\n".join(result))

solve()