def checked(idx, arr):

    for y in range(idx):
        res = 0
        for x in range(y, idx):
            res += arr[x]
            if board[y][x] == '+' and res <= 0:
                return False
            elif board[y][x] == '-' and res >= 0:
                return False
            elif board[y][x] == '0' and res != 0:
                return False
    return True


def solve(idx, arr):
    global flag
    if flag:
        return

    if not checked(idx, arr): 
        return

    if idx == N:
        flag = True
        print(*arr)
        return

    if board[idx][idx] == '-':
        for num in range(-10, 0):
            solve(idx+1, arr + [num])

    elif board[idx][idx] == '+':
        for num in range(1, 10+1):
            solve(idx+1, arr + [num])

    else:
        solve(idx+1, arr+[0])

N = int(input())
string = input()
idx = 0

board = [['x']*N for _ in range(N)]
for i in range(N):
    for j in range(i, N):
        if string[idx] == '-':
            board[i][j] = '-'
        elif string[idx] == '+':
            board[i][j] = '+'
        else:
            board[i][j] = '0'
        idx += 1

flag = False
result = []
solve(0, [])