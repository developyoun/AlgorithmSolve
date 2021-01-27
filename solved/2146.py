import sys
input = sys.stdin.readline
from collections import deque

def marking(initY, initX, color):
    queue = deque()
    queue.append([initY, initX])

    while queue:
        y, x = queue.popleft()
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if not 0 <= newY < N or not 0 <= newX < N: continue 
            if not board[newY][newX] or markBoard[newY][newX]: continue
            markBoard[newY][newX] = cnt
            queue.append([newY, newX])

def putBridge(Y, X, color):
    visited = [[0]*N for _ in range(N)]
    visited[Y][X] = 1
    queue = deque()
    queue.append([Y, X])

    while queue:
        y, x = queue.popleft()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < N and 0 <= new_x < N and not visited[new_y][new_x] and markBoard[new_y][new_x] != color:
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append([new_y, new_x])

                if markBoard[new_y][new_x]:
                    return visited[new_y][new_x]-1
    return result

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
markBoard = [[0]*N for _ in range(N)]

cnt = 1
for i in range(N):
    for j in range(N):
        if board[i][j] and not markBoard[i][j]:
            markBoard[i][j] = cnt
            marking(i, j, cnt)
            cnt += 1

result = float('INF')
for i in range(N):
    for j in range(N):
        if not board[i][j]: continue
        for r, c in ((i-1, j), (i, j-1), (i+1, j), (i, j+1)):
            if 0 <= r < N and 0 <= c < N:
                if markBoard[i][j] != markBoard[r][c]:
                    tmpValue = putBridge(r, c, markBoard[i][j])
                    result = min(tmpValue, result)

print(result)