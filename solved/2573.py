def melting():

    remove_ice = []
    rest_ice = []
    while ice:
        y, x = ice.pop()

        cnt = 0
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < row and 0 <= new_x < col:
                if not board[new_y][new_x]: cnt += 1
        if board[y][x] - cnt <= 0:
            remove_ice.append([y, x])
        else:
            board[y][x] -= cnt
            rest_ice.append([y, x])
    
    while remove_ice:
        y, x = remove_ice.pop()
        board[y][x] = 0
    
    return rest_ice

def div_check():
    visited = [[False]*col for _ in range(row)]

    check = 0
    for r, c in ice:
        if not visited[r][c]:
            visited[r][c] = True
            check += 1

            q = [[r, c]]
            while q:
                y, x = q.pop()
                for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_y, new_x = y+dy, x+dx
                    if 0 <= new_y < row and 0 <= new_x < col:
                        if board[new_y][new_x] and not visited[new_y][new_x]:
                            visited[new_y][new_x] = True
                            q.append([new_y, new_x])
            if check >= 2: return True
    return False


row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

ice = []
for i in range(row):
    for j in range(col):
        if board[i][j]: ice.append([i, j])

div_time = 0
while True:
    div_time += 1
    ice = melting()
    if not ice:
        div_time = 0
        break
    if div_check(): break
    
print(div_time)