import re

def find_min_number_in_string(s):
    numbers = re.findall(r'\d+', s)
    min_number = max(map(int, numbers))
    return min_number

T = int(input())
results = []

for _ in range(T):
    s = input()
    results.append(find_min_number_in_string(s))

for result in results:
    print(result)
