from collections import defaultdict, deque

N, M = map(int, input().split())
board = [[0]*(N+1) for _ in range(N+1)]
dic = defaultdict(list)

for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    dic[(sy, sx)].append((ey, ex))

visited = [[False]*(N+1) for _ in range(N+1)]
visited[1][1] = True
lights = [[0]*(N+1) for _ in range(N+1)]
lights[1][1] = 1

result = 1

q = deque()
q.append([1, 1])
while q:
    y, x = q.popleft()

    for yy, xx in dic[(y, x)]:
        lights[yy][xx] = 1
    
    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_y, new_x = y+dy, x+dx
        if 0 < new_y <= N and 0 < new_x <= N:
            if lights[new_y][new_x] and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                q.append([new_y, new_x])

print(sum(map(sum, lights)))