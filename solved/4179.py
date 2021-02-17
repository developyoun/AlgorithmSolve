from collections import deque

def solve():

    while pos:
        for _ in range(len(fires)):
            y, x = fires.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                newY, newX = y+dy, x+dx
                if 0 <= newY < row and 0 <= newX < col:
                    if board[newY][newX] != '#' and not burned[newY][newX]:
                        burned[newY][newX] = True
                        fires.append([newY, newX])

        for _ in range(len(pos)):
            y, x = pos.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                newY, newX = y+dy, x+dx
                if not (0 <= newY < row and 0 <= newX < col): return visited[y][x]+1
                if board[newY][newX] != '#' and visited[newY][newX] == -1 and not burned[newY][newX]:
                    visited[newY][newX] = visited[y][x]+1
                    pos.append([newY, newX])
                    
    return "IMPOSSIBLE"


row, col = map(int, input().split())
board = [input() for _ in range(row)]

visited = [[-1]*col for _ in range(row)]
burned = [[False]*col for _ in range(row)]

fires = deque()
pos = deque()
for i in range(row):
    for j in range(col):
        if board[i][j] == 'F': 
            fires.append([i, j])
            burned[i][j] = True
        elif board[i][j] == 'J': 
            pos.append([i, j])
            visited[i][j] = 0

print(solve())