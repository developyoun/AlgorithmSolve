from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solve(Y, X, D):
    visited = [[[0]*4 for _ in range(col)] for _ in range(row)]
    visited[Y][X][D] = 1

    queue = deque()
    queue.append([Y, X, D])

    while queue:
        y, x, d = queue.popleft()

        if [y, x, d] == [ey-1, ex-1, ed]:
            return visited[y][x][d]-1

        for k in range(1, 3+1):
            newY, newX = y+dy[d]*k, x+dx[d]*k
            if 0 <= newY < row and 0 <= newX < col:
                if board[newY][newX]: break
                if not visited[newY][newX][d]:
                    visited[newY][newX][d] = visited[y][x][d] + 1
                    queue.append([newY, newX, d])
        
        for dd in ((d+1)%4, (d-1)%4):
            if not visited[y][x][dd]:
                visited[y][x][dd] = visited[y][x][d] + 1
                queue.append([y, x, dd])


row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

sy, sx, sd = map(int, input().split())
ey, ex, ed = map(int, input().split())
dic = {1:1, 2:3, 3:2, 4:0}
sd, ed = dic[sd], dic[ed]
result = solve(sy-1, sx-1, sd)
print(result)