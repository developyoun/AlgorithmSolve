def dfs(idx):
    
    for new, val in range()
        

V = int(input())

connects = [[] for _ in range(V+1)]
for _ in range(V):
    info = list(map(int, input().split()))

    now_V = info[0]
    for v in range(1, len(info)-1, 2):
        connects[now_V].append([info[v], info[v+1]])

distance = [0] * (V+1)
for i in range(1, V+1):
    dfs(i)