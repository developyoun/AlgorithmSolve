from collections import deque
MAX = float('INF')
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
board = [input() for _ in range(N)]

sy, sx = -1, -1
ey, ex = -1, -1

visited = [[[MAX]*4 for _ in range(N)] for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(N):
        if board[i][j] == '#':
            if sy == -1 and sx == -1:
                sy, sx = i, j
                for k in range(4):
                    visited[i][j][k] = 0
                    q.append([i, j, k])
            else:
                ey, ex = i, j


while q:
    y, x, d = q.popleft()

    newY, newX = y+dy[d], x+dx[d]
    if 0 <= newY < N and 0 <= newX < N and board[newY][newX] != '*':
        if board[newY][newX] == '#' and visited[newY][newX][d] > visited[y][x][d]:
            visited[newY][newX][d] = visited[y][x][d]

        elif board[newY][newX] == '.':
            if visited[newY][newX][d] > visited[y][x][d]:
                q.append([newY, newX, d])
                visited[newY][newX][d] = visited[y][x][d]

        elif board[newY][newX] == '!':
            for nd in ((d+1)%4, d, (d-1)%4):
                if d == nd and visited[newY][newX][d] > visited[y][x][d]:
                    visited[newY][newX][d] = visited[y][x][d]
                    q.append([newY, newX, d])
                elif d != nd and visited[newY][newX][nd] > visited[y][x][d]+1:
                    visited[newY][newX][nd] = visited[y][x][d]+1
                    q.append([newY, newX, nd])

print(min(visited[ey][ex]))