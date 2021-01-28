from collections import deque

def checked(y, x):
    for r in range(y-1, y+2):
        for c in range(x-1, x+2):
            if board[r][c] == '1': return False
    return True

def solve(Y, X, D):
    visited = [[[-1, -1] for _ in range(N)] for _ in range(N)]
    visited[Y][X][D] = 0

    queue = deque()
    queue.append([Y, X, D])
    while queue:
        y, x, d = queue.popleft()

        if [y, x, d] == [ey, ex, ed]:
            return visited[y][x][d]

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = y+dy, x+dx
            if not d:   # d == 0 (가로)
                if 0 <= ny-1 and ny+1 < N and 0 <= nx < N and visited[ny][nx][d] == -1:
                    if board[ny][nx] != '1' and board[ny-1][nx] != '1' and board[ny+1][nx] != '1':
                        visited[ny][nx][d] = visited[y][x][d] + 1
                        queue.append([ny, nx, d])
            else:   # d == 1 (세로)
                if 0 <= ny < N and 0 <= nx-1 and nx+1 < N and visited[ny][nx][d] == -1:
                    if board[ny][nx] != '1' and board[ny][nx-1] != '1' and board[ny][nx+1] != '1':
                        visited[ny][nx][d] = visited[y][x][d] + 1
                        queue.append([ny, nx, d])

        nd = (d+1)%2
        if 1 <= y < N-1 and 1 <= x < N-1 and visited[y][x][nd] == -1 and checked(y, x):
            visited[y][x][nd] = visited[y][x][d] + 1
            queue.append([y, x, nd])
    return 0

    
N = int(input())
board = [list(input()) for _ in range(N)]

sy, sx, sd = -1, -1, -1
ey, ex, ed = -1, -1, -1
for i in range(N):
    for j in range(N):
        if board[i][j] == 'B' and sd == -1:
            if 0 <= i+1 < N and board[i+1][j] == 'B':
                sy, sx, sd = i+1, j, 0
            elif 0 <= j+1 < N and board[i][j+1] == 'B':
                sy, sx, sd = i, j+1, 1
        elif board[i][j] == 'E' and ed == -1:
            if 0 <= i+1 < N and board[i+1][j] == 'E':
                ey, ex, ed = i+1, j, 0
            elif 0 <= j+1 < N and board[i][j+1] == 'E':
                ey, ex, ed = i, j+1, 1

result = solve(sy, sx, sd)
print(result)