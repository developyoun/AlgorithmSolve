from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
inf = float('INF')

def solve():
    visited = [[[inf, inf, inf, inf] for _ in range(col)] for _ in range(row)]
    queue = deque()

    for i in range(4):
        visited[sy][sx][i] = 0
        queue.append([sy, sx, i])
    
    while queue:
        y, x, prev_direct = queue.popleft()

        for d in range(4):
            new_y, new_x = y+dy[d], x+dx[d]
            if 0 <= new_y < row and 0 <= new_x < col:
                if board[new_y][new_x] != '*':
                    if d == prev_direct and visited[new_y][new_x][d] > visited[y][x][prev_direct]:    # 1. 방향 같음
                        visited[new_y][new_x][d] = visited[y][x][d]
                        queue.append([new_y, new_x, d])
                    elif d != prev_direct and visited[new_y][new_x][d] > visited[y][x][prev_direct] + 1:   # 2. 방향 다름
                        visited[new_y][new_x][d] = visited[y][x][prev_direct] + 1
                        queue.append([new_y, new_x, d])
    return min(visited[ey][ex])
    

col, row = map(int, input().split())
board = [input() for _ in range(row)]

sy, sx, ey, ex = -1, -1, -1, -1
for i in range(row):
    for j in range(col):
        if board[i][j] == 'C':
            if [sy, sx] == [-1, -1]: sy, sx = i, j
            else: ey, ex = i, j

print(solve())