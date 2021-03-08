from collections import deque

def solve(Y, X):
    visited = [[False]*col for _ in range(row)]
    visited[Y][X] = True
    queue = deque()
    queue.append([Y, X])

    time = 0
    while queue:
        for _ in range(len(queue)):
            y, x = queue.popleft()

            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                newY, newX = y+dy, x+dx
                if 0 <= newY < row and 0 <= newX < col:
                    if board[newY][newX] == 'L' and not visited[newY][newX]:
                        visited[newY][newX] = True
                        queue.append([newY, newX])
        time += 1
    return time-1

row, col = map(int, input().split())
board = [input() for _ in range(row)]

start = []
for r in range(row):
    for c in range(col):
        if board[r][c] == 'L':
            cnt = 0
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                newR, newC = r+dy, c+dx
                if 0 <= newR < row and 0 <= newC < col:
                    if board[newR][newC] == 'L': cnt += 1
            
            if cnt <= 2:
                start.append([r, c])
result = 0
for r, c in start:
    result = max(result, solve(r, c))
print(result)