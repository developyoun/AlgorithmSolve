from collections import deque

s, e = map(int, input().split())
visited = [-1] * 200001
count = [0] * 200001
visited[s] = 0
count[s] = 1

dq = deque()
dq.append(s)
while dq:
    now = dq.popleft()

    for new in (now+1, now-1, now*2):
        if not 0 <= new < 200001: continue
        if visited[new] == -1:
            visited[new] = visited[now] +1
            count[new] += 1
            dq.append(new)
        elif visited[new] == visited[now]+1:
            count[new] += 1
            dq.append(new)

print(visited[e])
print(count[e])