dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
board = [[False]*101 for _ in range(101)]

def solve():

    for i in range(len(direct)-1, 0,-1):
        x, y = queue[-1]
        D = direct[i]
        newY, newX = y+dy[D], x+dx[D]

        if 0 <= newY <= 100 and 0 <= newX <= 100:
            board[newX][newY] = True
        queue.append([newX, newY])
        direct.append((D+1)%4)


for _ in range(int(input())):
    c, r, d, g = map(int, input().split())
    nr, nc = r+dy[d], c+dx[d]
    board[c][r] = True
    board[nc][nr] = True

    queue = [[c, r], [nc, nr]]
    direct = [d, (d+1)%4]
    for _ in range(g):
        solve()

cnt = 0
for row in range(100):
    for col in range(100):
        if board[col][row] and board[col][row+1] and board[col+1][row] and board[col+1][row+1]:
            cnt += 1
            
print(cnt)