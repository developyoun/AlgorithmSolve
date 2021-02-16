from collections import deque

def moveBall(y, x, dy, dx):
    cnt = 0
    newY, newX = y, x
    while 0 <= newY+dy < row and 0 <= newX+dx < col and board[newY+dy][newX+dx] != '#':
        cnt +=1
        newY, newX = newY+dy, newX+dx
        if board[newY][newX] == 'O': break
    return newY, newX, cnt


def solve(ry, rx, by, bx):
    visited = [[[[-1 for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]
    visited[ry][rx][by][bx] = 0

    queue = deque()
    queue.append([ry, rx, by, bx])
    while queue:
        redY, redX, blueY, blueX = queue.popleft()

        if visited[redY][redX][blueY][blueX] > 10: return 0
        if board[redY][redX] == 'O': return 1

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newRy, newRx, redMove = moveBall(redY, redX, dy, dx)
            newBy, newBx, blueMove = moveBall(blueY, blueX, dy, dx)

            if board[newBy][newBx] == 'O': continue
            
            if [newRy, newRx] == [newBy, newBx]:
                if redMove > blueMove:
                    newRy -= dy; newRx -= dx
                else:
                    newBy -= dy; newBx -= dx

            if visited[newRy][newRx][newBy][newBx] != -1: continue
            visited[newRy][newRx][newBy][newBx] = visited[redY][redX][blueY][blueX] + 1
            queue.append([newRy, newRx, newBy, newBx])
    return 0        


row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]

ry, rx = -1, -1
by, bx = -1, -1

for i in range(row):
    for j in range(col):
        if board[i][j] == 'R': 
            ry, rx = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B': 
            by, bx = i, j
            board[i][j] = '.'

print(solve(ry, rx, by, bx))