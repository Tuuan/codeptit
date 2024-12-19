def DFS(x, lst):
    lst[x] = True
    for i in adj[x]:
        if lst[i] == False:
            DFS(i, lst)
    return lst

n,m,x = map(int, input().split())
adj = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in adj:
        adj[u] = [v]
    else:
        adj[u].append(v)
    if v not in adj:
        adj[v] = [u]
    else:
        adj[v].append(u)
lst = {}
for i in range(n):
    lst[i+1] = False
lst = DFS(x, lst)
for i in lst:
    if lst[i] == False:
        print(i)
