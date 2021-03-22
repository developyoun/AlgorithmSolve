from collections import deque

def solve(Y, X):
    q = deque()
    q.append([Y, X])
    time = 0
    while q:
        time += 1
        for _ in range(len(q)):
            y, x = q.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)):
                newY, newX = y+dy, x+dx
                if 0 <= newY < row and 0 <= newX < col and not visited[newY][newX]:
                    visited[newY][newX] = True
                    if board[newY][newX]: return time
                    else: q.append([newY, newX])
    return time     


row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

arr = []
for i in range(row):
    for j in range(col):
        if not board[i][j]:
            arr.append([i, j])
result = 0
for y, x in arr:
    visited = [[False]*col for _ in range(row)]
    visited[y][x] = True

    val = solve(y, x)
    result = max(result, val)

print(result)