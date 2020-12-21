N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(int(input())):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

q = [1]
visited = [False] * (N+1)
visited[1] = True
while q:
    node = q.pop()

    for new in arr[node]:
        if not visited[new]:
            visited[new] = True
            q.append(new)
print(visited.count(True)-1)