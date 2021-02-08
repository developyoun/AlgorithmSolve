from collections import deque
inf = float('INF')
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solve(Y, X):
    visited = [[[inf, inf] for _ in range(col)] for _ in range(row)]
    init = table[Y][X]
    visited[Y][X] = [0, init]

    queue = deque()
    queue.append([Y, X, 0, init])

    while queue:
        y, x, v1, v2 = queue.popleft()

        for d in range(4):
            newY, newX = y+dy[d], x+dx[d]
            if 0 <= newY < row and 0 <= newX < col:

                newV1, newV2 = visited[newY][newX]
                V2 = v2+table[newY][newX]
                
                if board[newY][newX] in ('.', 'F'):
                    if newV1 > v1 or (newV1 == v1 and newV2 > V2):
                        visited[newY][newX] = [v1, V2]
                        queue.append([newY, newX, v1, V2])
                elif board[newY][newX] == 'g':
                    if newV1 > v1+1 or (newV1 == v1+1 and newV2 > V2):
                        visited[newY][newX] = [v1+1, V2]
                        queue.append([newY, newX, v1+1, V2])

    # print(visited[ey][ex])
    return visited[ey][ex]

row, col = map(int, input().split())
board = [input() for _ in range(row)]
table = [[0]*col for _ in range(row)]

sy, sx = -1, -1
ey, ex = -1, -1
for r in range(row):
    for c in range(col):
        if board[r][c] == 'S':
            sy, sx = r, c
        elif board[r][c] == 'F':
            ey, ex = r, c
        elif board[r][c] == 'g':
            for D in range(4):
                ny, nx = r+dy[D], c+dx[D]
                if 0 <= ny < row and 0 <= nx < col and board[ny][nx] == '.':
                    table[ny][nx] = 1

res1, res2 = solve(sy, sx)
print(res1, res2)