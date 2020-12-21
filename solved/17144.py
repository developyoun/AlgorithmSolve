def spread():
    q = []
    for r in range(row):
        for c in range(col):
            if board[r][c] >= 5:
                q.append([r, c, board[r][c]])

    while q:
        y, x, val = q.pop()
        
        cnt, new_val = 0, val//5
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < row and 0 <= new_x < col and board[new_y][new_x] >= 0:
                board[new_y][new_x] += new_val
                cnt += new_val
        board[y][x] -= cnt


def cleaning(up, down):
    res = 0

    y, x = up[0], up[1]+1
    prev, board[y][x] = board[y][x], 0
    while x+1 < col: board[y][x+1], prev = prev, board[y][x+1]; x += 1
    while 0 <= y-1: board[y-1][x], prev = prev, board[y-1][x]; y-=1
    while 0 <= x-1: board[y][x-1], prev = prev, board[y][x-1]; x-=1
    while board[y+1][x] != -1: board[y+1][x], prev = prev, board[y+1][x]; y+=1
    res += prev

    y, x = down[0], down[1]+1
    prev, board[y][x] = board[y][x], 0
    while x+1 < col: board[y][x+1], prev = prev, board[y][x+1]; x += 1
    while y+1 < row: board[y+1][x], prev = prev, board[y+1][x]; y+=1
    while 0 <= x-1: board[y][x-1], prev = prev, board[y][x-1]; x-=1
    while board[y-1][x] != -1: board[y-1][x], prev = prev, board[y-1][x]; y-=1
    res += prev

    return res

row, col, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
cleaner = []

total = 0
for i in range(row):
    for j in range(col):
        if board[i][j] == -1: cleaner.append([i, j])
        else: total += board[i][j]

for _ in range(K):
    spread()
    total -= cleaning(cleaner[0], cleaner[1])

print(total)