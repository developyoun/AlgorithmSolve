from collections import deque

N = int(input())
visited = [-1] * (N+1)
visited[N] = 0
index_arr = [-1] * N

queue = deque([N])
while queue:
    now = queue.popleft()

    if now == 1:
        break

    if not now % 3 and visited[now//3] == -1:
        new = now // 3
        visited[new] = visited[now]+1
        index_arr[new] = now
        queue.append(new)
    if not now % 2 and visited[now//2] == -1:
        new = now // 2
        visited[new] = visited[now]+1
        index_arr[new] = now
        queue.append(new)
    if now-1 > 0 and visited[now - 1] == -1:
        new = now-1
        visited[new] = visited[now]+1
        index_arr[new] = now
        queue.append(new)

answer = deque([1])
idx = 1
while answer[0] != N:
    answer.appendleft(index_arr[idx])
    idx = index_arr[idx]
print(visited[1])
print(*answer)