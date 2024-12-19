class Subject:
    def __init__(self,id,sub,method):
        self.id = id
        self.sub = sub
        self.method = method
    
    def __str__(self):
        return "{} {} {}".format(self.id, self.sub, self.method)

list = []
for _ in range(int(input())):
    id = input()
    sub = input()
    method = input()
    list.append(Subject(id,sub,method))

list.sort(key = lambda x: x.id)
print(*list, sep="\n")
    
