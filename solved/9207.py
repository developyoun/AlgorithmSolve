import sys
input = sys.stdin.readline

def solve(val, cnt):
    global res1, res2

    if val < res1:
        res1 = val
        res2 = cnt
    elif val == res1:
        if cnt < res2:
            res2 = cnt
    
    for y in range(5):
        for x in range(9):
            if board[y][x] == 'o':
                for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    newYY, newXX, newY, newX = y+dy*2, x+dx*2, y+dy, x+dx
                    if 0 <= newYY < 5 and 0 <= newXX < 9 and board[newY][newX] == 'o' and board[newYY][newXX] == '.':
                        board[y][x], board[newY][newX], board[newYY][newXX] = '.', '.', 'o'
                        solve(val-1, cnt+1)
                        board[y][x], board[newY][newX], board[newYY][newXX] = 'o', 'o', '.'


for _ in range(int(input())):
    board = [list(input()) for _ in range(5)]
    total = 0
    for i in range(5):
        for j in range(9):
            if board[i][j] == 'o':
                total += 1

    res1, res2 = 46, 46
    solve(total, 0)
    print(res1, res2)
    input()