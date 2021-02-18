from collections import defaultdict
dy = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dx = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

def move_crazy(ty, tx):
    save = defaultdict(int)
    while crazy:
        y, x = crazy.pop()
        board[y][x] = '.'

        direct, distance = -1, 100001
        for d in (1, 2, 3, 4, 6, 7, 8, 9):
            ny, nx = y+dy[d], x+dx[d]
            if 0 <= ny < row and 0 <= nx < col:
                dis = abs(ny-ty) + abs(nx-tx) 
                if dis < distance:
                    distance = dis
                    direct = d
        save[(y+dy[direct], x+dx[direct])] += 1

    for key, value in save.items():
        y, x = key
        if [y, x] == [ty, tx]: return False
        if value > 1:
            continue
        else:
            crazy.append([y, x])
            board[y][x] = 'R'
    return True

row, col = map(int, input().split())
board = [list(input()) for _ in range(row)]

crazy = []
sy, sx = -1, -1
for i in range(row):
    for j in range(col):
        if board[i][j] == 'I':
            sy, sx = i, j
            board[i][j] = '.'
        elif board[i][j] == 'R':
            crazy.append([i, j])

cnt, flag = 0, False
for number in input():
    num = int(number)
    newY, newX = sy+dy[num], sx+dx[num]

    cnt += 1
    if not (0 <= newY < row and 0 <= newX < col) or board[newY][newX] == 'R':
        flag = True
        break
    
    if not move_crazy(newY, newX):
        flag = True
        break
    
    sy, sx = newY, newX

if not flag:
    board[sy][sx] = 'I'
    for a in board:
        print(''.join(a))
else:
    print("kraj {}".format(cnt))