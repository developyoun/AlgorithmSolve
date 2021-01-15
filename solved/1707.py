dic = {1: -1, -1: 1}

def is_BG(init):
    visited[init] = 1
    q = [init]
    
    while q:
        now = q.pop()

        for new in edge[now]:
            if not visited[new]:
                visited[new] = dic[visited[now]]
                q.append(new)
            elif visited[new] == visited[now]:
                return False

    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    edge = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)

    visited = [0] * (V+1)
    flag = True
    for idx in range(1, V+1):
        if visited[idx]: continue

        flag = is_BG(idx)
        if not flag:
            break
    
    print("YES" if flag else "NO")