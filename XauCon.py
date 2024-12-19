def count_substrings(N, M, s):
    len_s = len(s)
    if N < len_s:
        return 0
    num_positions = N - len_s + 1
    num_ways = pow(26, N - len_s, M)
    result = (num_positions * num_ways) % M
    return result

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        M = int(data[index + 1])
        s = data[index + 2]
        index += 3
        
        result = count_substrings(N, M, s)
        results.append(result)
    
    for result in results:
        print(result)
solve()