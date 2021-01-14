def melting_cheese():
    res = 0
    visited = [[False]*col for _ in range(row)]
    visited[0][0] = True
    save = []

    q = [[0, 0]]
    while q:
        y, x = q.pop()
        
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < row and 0 <= new_x < col and not visited[new_y][new_x]:
                visited[new_y][new_x] = True

                if not board[new_y][new_x]:
                    q.append([new_y, new_x])
                else:
                    save.append([new_y, new_x])

    res += len(save)
    while save:
        y, x = save.pop()
        board[y][x] = 0
        
    return res

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

cnt = 0
for i in range(row):
    for j in range(col):
        if board[i][j]: cnt += 1

time = 0
while True:
    time += 1
    melted = melting_cheese()
    if not cnt - melted:
        print(time)
        print(melted)
        break
    cnt -= melted