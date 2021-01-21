def solve():
    global flag
    if flag: return

    if not blank:
        flag = True
        for b in board:
            print(*b)
        return
    
    node_y, node_x = blank.pop()
    std_y, std_x = node_y//3, node_x//3
    for n in range(1, 10):
        if not row[node_y][n] and not col[node_x][n] and not square[std_y][std_x][n]:
            row[node_y][n] = col[node_x][n] = square[std_y][std_x][n] = True
            board[node_y][node_x] = n
            solve()
            board[node_y][node_x] = 0
            row[node_y][n] = col[node_x][n] = square[std_y][std_x][n] = False
    blank.append([node_y, node_x])


board = [list(map(int, input().split())) for _ in range(9)]

row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
square = [[[False]*10 for _ in range(3)] for _ in range(3)]

blank = []
for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        for y in range(i, i+3):
            for x in range(j, j+3):
                if not board[y][x]:
                    blank.append([y, x])
                else:
                    row[y][board[y][x]] = True
                    col[x][board[y][x]] = True
                    square[y//3][x//3][board[y][x]] = True
flag = False
solve()