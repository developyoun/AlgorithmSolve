dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def CanConnect(y, x, d):
    while 0 <= y+dy[d] < N and 0 <= x+dx[d] < N:
        newY, newX = y+dy[d], x+dx[d]
        if board[newY][newX] or line[newY][newX]: return False
        y, x = newY, newX
    return True

def connect(y, x, d):
    length = 0
    while 0 <= y+dy[d] < N and 0 <= x+dx[d] < N:
        newY, newX = y+dy[d], x+dx[d]
        line[newY][newX] = True
        length += 1
        y, x = newY, newX
    return length

def disconnect(y, x, d):
    while 0 <= y+dy[d] < N and 0 <= x+dx[d] < N:
        newY, newX = y+dy[d], x+dx[d]
        line[newY][newX] = False
        y, x = newY, newX
    return

def connectLine(idx, cnt, lengthLine):
    global totalCnt, resultLine
    if idx == num:
        if cnt > totalCnt:
            totalCnt = cnt
            resultLine = lengthLine
        elif cnt == totalCnt:
            resultLine = min(lengthLine, resultLine)
        return

    y, x = queue[idx]
    for direct in range(4):
        if CanConnect(y, x, direct):
            l = connect(y, x, direct)
            connectLine(idx+1, cnt+1, lengthLine+l)
            disconnect(y, x, direct)
            
    connectLine(idx+1, cnt, lengthLine)

for case in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    queue = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j]:
                queue.append([i, j])

    num = len(queue)
    
    totalCnt, resultLine = 0, N*N

    line = [[False]*N for _ in range(N)]
    connectLine(0, 0, 0)

    print('#{} {}'.format(case, resultLine))