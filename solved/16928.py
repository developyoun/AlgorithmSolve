from collections import deque

N, S = map(int, input().split())
arr = [0] * 101
for _ in range(N+S):
    s, e = map(int, input().split())
    arr[s] = e

visited = [0] * 101
visited[1] = 1
q = deque()
q.append(1)

while q:
    now = q.popleft()

    if now == 100: break

    for i in range(1, 7):
        new = now + i
        if 0 <= new <= 100 and not visited[new]:
            if arr[new] and not visited[arr[new]]:
                moveNew = arr[new]
                visited[moveNew] = visited[now] + 1
                q.append(moveNew)

            elif not arr[new]:
                visited[new] = visited[now] + 1
                q.append(new)
print(visited[100]-1)