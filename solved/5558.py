from collections import deque

def solve(Y, X, target):
    visited = [[-1]*col for _ in range(row)]
    visited[Y][X] = 0
    queue = deque()
    queue.append([Y, X])

    while queue:
        y, x = queue.popleft()

        if board[y][x] == target:
            return y, x, visited[y][x]

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < row and 0 <= newX < col:
                if visited[newY][newX] == -1 and board[newY][newX] != 'X':
                    visited[newY][newX] = visited[y][x] + 1
                    queue.append([newY, newX])
    

row, col, N = map(int, input().split())
board = [input() for _ in range(row)]

sy, sx = -1, -1
for r in range(row):
    for c in range(col):
        if board[r][c] == 'S':
            sy, sx = r, c

result = 0
for i in range(1, N+1):
    sy, sx, cnt = solve(sy, sx, str(i))
    result += cnt
print(result)