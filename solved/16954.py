dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 0, 1, 1, 1, 0, -1, -1, -1]

def move():
    tmp, flag = set(), False
    for y, x in q:
        if board[y][x] == '#': continue
        for i in range(9):
            newY, newX = y+dy[i], x+dx[i]
            if 0 <= newY < 8 and 0 <= newX < 8 and board[newY][newX] != '#':
                tmp.add((newY, newX))
    return tmp

def wall_down():
    for x in range(8):
        for y in range(7, 0, -1):
            board[y][x] = board[y-1][x]
        board[0][x] = '.'


board = [list(input()) for _ in range(8)]
q = {(7, 0)}
for _ in range(8):
    q = move()
    wall_down()
    
if q:
    print(1)
else:
    print(0)