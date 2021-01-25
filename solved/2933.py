from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
inf = float('INF')

def putDown(H, arr):
    saveArr = []

    for C in range(col):
        for R in range(row):
            if arr[R][C]:
                saveArr.append([R, C])
                board[R][C] = '.'
        
        while saveArr:
            R, C = saveArr.pop()
            board[R+H][C] = 'x'
        
    return

def bfs(startY, startX):
    saveHeightsArr = [-1] * col
    saveHeightsArr[startX] = startY

    visited = [[False]*col for _ in range(row)]
    visited[startY][startX] = True

    queue = deque()
    queue.append([startY, startX])

    while queue:
        y, x = queue.popleft()

        for d in range(4):
            newY, newX = y + dy[d], x + dx[d]
            if 0 <= newY < row and 0 <= newX < col:
                if not visited[newY][newX] and board[newY][newX] == 'x':
                    visited[newY][newX] = True
                    saveHeightsArr[newX] = max(saveHeightsArr[newX], newY)
                    queue.append([newY, newX])
    putDownNum = inf
    for X in range(col):
        Y, cnt = saveHeightsArr[X]+1, 0
        if not Y: continue
        while 1 <= Y + cnt < row and board[Y+cnt][X] != 'x':
            cnt += 1
        putDownNum = min(putDownNum, cnt)

    if putDownNum != inf:
        putDown(putDownNum, visited)

    return


def brokeMineral(init_y, init_x):
    board[init_y][init_x] = '.'

    for d in range(4):
        sideY, sideX = init_y + dy[d], init_x + dx[d]
        if 0 <= sideY < row and 0 <= sideX < col:
            if board[sideY][sideX] == 'x':
                bfs(sideY, sideX)


row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]

N = int(input())
heights = list(map(int, input().split()))

for i in range(N):
    height = row - heights[i]

    if not i & 1: # 짝수
        for c in range(col):
            if board[height][c] == 'x':
                brokeMineral(height, c)
                break
    else: # 홀수
        for c in range(col-1, -1, -1):
            if board[height][c] == 'x':
                brokeMineral(height, c)
                break

for b in board:
    print(''.join(b))