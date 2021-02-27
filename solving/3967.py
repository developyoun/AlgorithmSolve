from itertools import permutations

def check(p):
    flag = True

    for k in range(len(p)):
        r, c = arr[k]
        board[r][c] = p[k]
    
    for y in (1, 3):
        total = 0
        for x in range(1, 9, 2):
            total += board[y][x]
        if total != 26: flag = False

    total1, total2 = 0, 0
    for y in range(4):
        total1 += board[y][4-y]
        total2 += board[y][4+y]
    if total1 != 26 or total2 != 26: flag = False

    total1, total2 = 0 ,0
    for y in range(1, 5):
        total1 += board[y][y]
        total2 += board[y][8-y]
    if total1 != 26 or total2 != 26: flag = False

    if not flag:
        for k in range(len(p)):
            r, c = arr[k]
            board[r][c] = 'x'

    return flag

board = [list(input()) for _ in range(5)]
dic = {chr(64+i): i for i in range(1, 13)}
s = [i for i in range(1, 13)]
arr = []

for i in range(5):
    for j in range(9):
        if board[i][j] == '.': continue

        if board[i][j] == 'x':
            arr.append([i, j])
        else:
            s.remove(dic[board[i][j]])
            board[i][j] = dic[board[i][j]]

cnt = 0
for perm in permutations(s, len(s)):
    if check(perm):
        for i in range(5):
            for j in range(9):
                if board[i][j] != '.':
                    board[i][j] = chr(64+board[i][j])
        break

for a in board:
    print(''.join(a))