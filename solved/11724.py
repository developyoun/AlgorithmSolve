V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

result = 0

visited = [False] * (V+1)
for i in range(1, V+1):
    if not visited[i]:
        visited[i] = True
        result += 1
        q = [i]
        while q:
            now = q.pop()
            for new in arr[now]:
                if not visited[new]:
                    visited[new] = True
                    q.append(new)
print(result)