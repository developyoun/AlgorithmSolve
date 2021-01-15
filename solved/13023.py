def search(idx, cnt):
    global result 

    if result:
        return

    if cnt >= 4:
        result = 1
        return

    for new in arr[idx]:
        if not visited[new]:
            visited[new] = True
            search(new, cnt+1)
            visited[new] = False

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * N
result = 0
for i in range(N):
    visited[i] = True
    search(i, 0)
    visited[i] = False
print(result)