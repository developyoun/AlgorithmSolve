from collections import deque

MAX = float('INF')
s = int(input())
visited = [[MAX]*1001 for _ in range(1001)]
visited[1][0] = 0

queue = deque([[1, 0]])
while queue:
    now, clip = queue.popleft()


    if visited[now][now] == MAX:
        visited[now][now] = visited[now][clip] + 1
        queue.append([now, now])

    if now+clip <= s and visited[now+clip][clip] == MAX:
        visited[now+clip][clip] = visited[now][clip] + 1
        queue.append([now+clip, clip])
    
    if now-1 and visited[now-1][clip] == MAX:
        visited[now-1][clip] = visited[now][clip] + 1
        queue.append([now-1, clip])

print(min(visited[s]))