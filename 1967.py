def bfs(start):
    visited = [-1] * (N+1)
    visited[start] = 0
    q = [start]
    while q:
        node = q.pop()

        for new_node, distance in info[node]:
            if visited[new_node] == -1:
                visited[new_node] = visited[node] + distance
                q.append(new_node)
    return visited, max(visited)

N = int(input())
info = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, v = map(int, input().split())
    info[a].append([b, v])
    info[b].append([a, v])

arr, MAX_distance = bfs(1)
new_node = arr.index(MAX_distance)
__, result = bfs(new_node)
print(result)