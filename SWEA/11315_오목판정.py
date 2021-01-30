def rowCheck(y, x):
    cnt = 1
    while 0 <= y < N and 0 <= x+1 < N and board[y][x+1] == 'o':
        cnt, x = cnt+1, x+1
    return True if cnt >= 5 else False


def colCheck(y, x):
    cnt = 1
    while 0 <= y+1 < N and 0 <= x < N and board[y+1][x] == 'o':
        cnt, y = cnt+1, y+1
    return True if cnt >= 5 else False


def diagonalCheck(y, x):
    cnt = 1
    while 0 <= y+1 < N and 0 <= x+1 < N and board[y+1][x+1] == 'o':
        cnt, y, x = cnt+1, y+1, x+1
    if cnt >= 5:
        return True

    cnt = 1
    while 0 <= y+1 < N and 0 <= x-1 < N and board[y+1][x-1] == 'o':
        cnt, y, x = cnt+1, y+1, x-1
    return True if cnt >= 5 else False


def solve():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o' and (rowCheck(i, j) or colCheck(i, j) or diagonalCheck(i, j)):
                return True
    return False

for case in range(1, int(input())+1):
    N = int(input())
    board = [input() for _ in range(N)]

    flag = solve()
    print('#{} {}'.format(case, 'YES' if flag else 'NO'))