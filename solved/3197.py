from collections import deque

def melting():
    tmp = deque()

    while ice:
        y, x = ice.popleft()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < row and 0 <= newX < col and not waters[newY][newX]:
                if board[newY][newX] == 'X':
                    board[newY][newX] = '.'
                    waters[newY][newX] = True
                    tmp.append([newY, newX])
    return tmp


def findSwan():
    tmp = deque()

    while swan:
        y, x = swan.popleft()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < row and 0 <= newX < col and not visited[newY][newX]:
                visited[newY][newX] = True
                if board[newY][newX] == 'L':
                    return True, []
                elif board[newY][newX] == 'X':
                    tmp.append([newY, newX])
                else:
                    swan.append([newY, newX])
    return False, tmp


row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]

waters = [[False]*col for _ in range(row)]
visited = [[False]*col for _ in range(row)]

swan = deque()
ice = deque()
for i in range(row):
    for j in range(col):
        if board[i][j] == '.' or board[i][j] == 'L':
            for newI, newJ in ((i+1, j), (i, j+1), (i-1, j), (i, j-1)):
                if 0 <= newI < row and 0 <= newJ < col and board[newI][newJ] == 'X':
                    ice.append([i, j])
                    waters[i][j] = True
                    break

        if board[i][j] == 'L':
            if not swan:
                visited[i][j] = True
                swan.append([i, j])
            else:
                ey, ex = i, j

time = 0
while True:
    flag, swan = findSwan()
    if flag: break
    ice = melting()
    time += 1

print(time)