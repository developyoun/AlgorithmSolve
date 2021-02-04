from collections import deque

N, s, g, u, d = map(int, input().split())
visited = [-1]*(N+1)
visited[s] = 0
dq = deque([s])

while dq:
    now = dq.popleft()

    if now == g:
        break

    for new in (now+u, now-d):
        if 1 <= new <= N and visited[new] == -1:
            visited[new] = visited[now] + 1
            dq.append(new)

print("use the stairs" if visited[g] == -1 else visited[g])