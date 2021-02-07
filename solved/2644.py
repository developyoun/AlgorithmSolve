from collections import deque

N = int(input())
arr = [[] for _ in range(N+1)]
s, e = map(int, input().split())
for _ in range(int(input())):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [-1]*(N+1)
visited[s] = 0
queue = deque()
queue.append(s)

while queue:

    now = queue.popleft()
    if now == e: break

    for new in arr[now]:
        if visited[new] == -1:
            visited[new] = visited[now] + 1
            queue.append(new)

print(visited[e])