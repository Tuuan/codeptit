n = int(input())
student = []
for _ in range(n):
    name = input()
    c,s = map(int, input().split())
    student.append((name,c,s))

student.sort(key=lambda x: (-x[1],x[2],x[0]))
for i in student:
    print(i[0],i[1],i[2])
        