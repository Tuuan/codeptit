n = int(input())
a = [int(i) for i in input().split()]
max_sum = max_sum_temp = a[0]
max_left = max_right = left = 0
for i in range(1, n):
    if a[i] > max_sum_temp + a[i]:
        max_sum_temp = a[i]
        left = i
    else:
        max_sum_temp += a[i]
    if max_sum_temp > max_sum:
        max_sum = max_sum_temp
        max_left = left
        max_right = i
print(max_left + 1, max_right + 1, max_sum)