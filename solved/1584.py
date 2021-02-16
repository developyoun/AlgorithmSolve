from collections import deque
import sys
input = sys.stdin.readline

inf = float('INF')

def dangerZone(sy, sx, ey, ex, num):
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            board[y][x] = num

board = [[0]*501 for _ in range(501)]
for _ in range(int(input())):
    y1, x1, y2, x2 = map(int, input().split())
    sy, sx, ey, ex = min(y1, y2), min(x1, x2), max(y1, y2), max(x1, x2)
    dangerZone(sy, sx, ey, ex, 1)

for _ in range(int(input())):
    y1, x1, y2, x2 = map(int, input().split())
    sy, sx, ey, ex = min(y1, y2), min(x1, x2), max(y1, y2), max(x1, x2)
    dangerZone(sy, sx, ey, ex, 2)

visited = [[inf]*501 for _ in range(501)]
visited[0][0] = 0

queue = deque()
queue.append([0, 0, 0])

while queue:
    y, x, m = queue.popleft()

    if [y, x] == [500, 500]:
        break

    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        newY, newX = y+dy, x+dx
        if not (0 <= newY <= 500 and 0 <= newX <= 500) or board[newY][newX] == 2: continue
        if not board[newY][newX] and visited[newY][newX] > m:
            visited[newY][newX] = m
            queue.appendleft([newY, newX, m])
        elif board[newY][newX] == 1 and visited[newY][newX] > m+1:
            visited[newY][newX] = m+1
            queue.append([newY, newX, m+1])

result = visited[500][500]
print(-1 if result == inf else result)