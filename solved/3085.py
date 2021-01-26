def calc(y, x):
    best, color = 0, board[y][x]

    cntLeft, cntRight = 0, 0
    while 0 <= x - cntLeft - 1 < N and board[y][x-cntLeft-1] == color:
        cntLeft += 1
    while 0 <= x + cntRight + 1 < N and board[y][x+cntRight+1] == color:
        cntRight += 1

    cntUp, cntDown = 0, 0
    while 0 <= y - cntUp - 1 < N and board[y-cntUp-1][x] == color:
        cntUp += 1
    while 0 <= y + cntDown + 1 < N and board[y+cntDown+1][x] == color:
        cntDown += 1
    return max(cntLeft + cntRight + 1, cntUp + cntDown + 1)    


N = int(input())
board = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(N):
        if i + 1 < N:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            result = max(result, calc(i, j))
            result = max(result, calc(i+1, j))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

        if j + 1 < N:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            result = max(result, calc(i, j))
            result = max(result, calc(i, j+1))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
print(result)