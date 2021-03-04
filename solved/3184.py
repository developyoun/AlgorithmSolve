def search(Y, X):
    visited[Y][X] = True
    q = [[Y, X]]

    S, W = 0, 0
    while q:
        y, x = q.pop()

        if board[y][x] == 'v': 
            W += 1
        if board[y][x] == 'o': 
            S += 1

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < row and 0 <= newX < col:
                if board[newY][newX] != '#' and not visited[newY][newX]:
                    visited[newY][newX] = True
                    q.append([newY, newX])
    if S > W:
        W = 0
    else:
        S = 0
    return S, W

row, col = map(int, input().split())
board = [input() for _ in range(row)]
visited = [[False]*col for _ in range(row)]

sheep, wolf = 0, 0
for i in range(row):
    for j in range(col):
        if not visited[i][j] and board[i][j] != '#':
            s, w = search(i, j)
            sheep += s
            wolf += w
print(sheep, wolf)