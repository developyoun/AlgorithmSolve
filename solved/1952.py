dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

row, col = map(int, input().split())
y, x = 0, 0
board = [[False]*col for _ in range(row)]
board[y][x] = True

d, cnt = 0, 0
for _ in range(row*col-1):
    if not 0 <= y+dy[d] < row or not 0 <= x+dx[d] < col or board[y+dy[d]][x+dx[d]]: 
        cnt += 1
        d = (d+1)%4
    y, x = y+dy[d], x+dx[d]
    board[y][x] = True

print(cnt)