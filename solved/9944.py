dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def init(board):
    cnt = 0
    for r in range(row):
        for c in range(col):
            if board[r][c] == '.':
                cnt += 1
    return cnt

def solve(y, x, cnt, turn):
    global result

    if turn >= result:
        return

    if cnt >= cntBlank:
        if cnt == cntBlank:
            result = min(result, turn)
        return

    for d in range(4):
        newY, newX, tmp = y, x, 0
        while 0 <= newY+dy[d] < row and 0 <= newX+dx[d] < col and board[newY+dy[d]][newX+dx[d]] == '.' and not visited[newY+dy[d]][newX+dx[d]]:
            newY += dy[d]; newX += dx[d]
            visited[newY][newX] = True
            tmp += 1
        if tmp: solve(newY, newX, cnt+tmp, turn+1)

        while tmp:
            visited[newY][newX] = False
            newY -= dy[d]; newX -= dx[d]
            tmp -= 1


import sys
input = sys.stdin.readline

num = 1
while True:
    INPUT = input().rstrip()
    if INPUT == '': break
    row, col = map(int, INPUT.split())
    board = [input() for _ in range(row)]

    cntBlank = init(board)
    result = 10**6

    visited = [[False]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if board[i][j] == '.':
                visited[i][j] = True
                solve(i, j, 1, 0)
                visited[i][j] = False
    print('Case {}: {}'.format(num, -1 if result==10**6 else result))
    num += 1