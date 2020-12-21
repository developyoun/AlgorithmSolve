from collections import deque
pos, goal = map(int, input().split())
visited  = [-1] * 200001
time, cnt = float('INF'), 0

visited[pos] = 0
queue = deque()
queue.append([pos, 0])

while queue:

    for _ in range(len(queue)): 
        now, t = queue.popleft()

        if t > time:
            continue

        if now == goal:
            if time > t:
                time = t;
            cnt += 1
            continue

        for new in (now+1, now-1, now*2):
            if new < 0 or new > 200000: continue
            if visited[new] == -1:
                visited[new] 
        
print(time, cnt)