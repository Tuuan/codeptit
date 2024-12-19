t = int(input())
for j in range (t):
    n=int(input())
    list =sorted([int(i) for i in input().split()])
    count=0
    for i in range(0,n-2):
        left = i+1
        right = n-1
        a = list[i]+list[left]+list[right]
        while left<right:
            a = list[i]+list[left]+list[right]
            if not a:
                count+=1
                left+=1
            elif a < 0:
                left+=1
            else:
                right-=1
    print(count)