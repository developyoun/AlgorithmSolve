from collections import deque

def spread_out_air(init_y, init_x):
    dq = deque()

    board[init_y][init_x] = -1
    dq.append([init_y, init_x])
    while dq:
        y, x = dq.popleft()
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            
            new_y, new_x = y+dy, x+dx
            if not 0 <= new_y < row or not 0 <= new_x < col or board[new_y][new_x]: continue
            board[new_y][new_x] = -1
            dq.append([new_y, new_x])
    
def del_cheese():
    
    tmp, rest = [], []
    while cheeses:
        y, x = cheeses.pop()

        cnt = 0
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < row and 0 <= new_x < col and board[new_y][new_x] == -1: cnt += 1

        if cnt >= 2: tmp.append([y, x])
        else: rest.append([y, x])
    
    while tmp:
        y, x = tmp.pop()
        spread_out_air(y, x)

    return rest


row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

spread_out_air(0, 0)

cheeses = []
for i in range(row):
    for j in range(col):
        if board[i][j] == 1: cheeses.append([i, j])

time = 0
while True:
    cheeses = del_cheese()[:]
    time += 1
    if not cheeses: break
print(time)