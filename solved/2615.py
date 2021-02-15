dy = [-1, 0, 1, 1]
dx = [1, 1, 1, 0]

board = [list(map(int, input().split())) for _ in range(19)]

def solve(y, x):
    num = board[y][x]
    for d in range(4):
        revY, revX = y-dy[d], x-dx[d]
        if not (0 <= revY < 19 and 0 <= revX < 19) or not board[revY][revX] or board[revY][revX] != num:
            newY, newX, cnt = y+dy[d], x+dx[d], 1
            while 0 <= newY < 19 and 0 <= newX < 19 and board[newY][newX] == num:
                newY += dy[d]; newX += dx[d]
                cnt += 1
            if cnt == 5:
                return True
    return False

flag, r, c = False, -1, -1
for i in range(19):
    for j in range(19):
        if board[i][j]:
            if solve(i, j):
                flag, r, c = True, i, j
                break
    if flag: break
                

if [r, c] != [-1, -1]:
    print(board[r][c])
    print(r+1, c+1)
else:
    print(0)