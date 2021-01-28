from collections import deque

def searchLight(Y, X):
    flag = 0
    visited = [[False]*N for _ in range(N)]
    visited[Y][X] = True
    queue = deque()
    queue.append([Y, X])

    while queue:
        y, x = queue.popleft()

        if not alreadyTurnOn[y][x]:
            alreadyTurnOn[y][x] = True
            for ny, nx in arr[y][x]:
                if not lights[ny][nx]: flag += 1
                lights[ny][nx] = True

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < N and 0 <= newX < N and not visited[newY][newX] and lights[newY][newX]:
                visited[newY][newX] = True
                queue.append([newY, newX])
    return flag

N, M = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    sy, sx, ey, ex = map(int, input().split())
    arr[sy-1][sx-1].append([ey-1, ex-1])


alreadyTurnOn = [[0]*N for _ in range(N)]
lights = [[0]*N for _ in range(N)]
lights[0][0] = True
cnt = 1
while True:
    result = searchLight(0, 0)
    if not result: break
    cnt += result
print(cnt)