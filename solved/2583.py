row, col, N = map(int, input().split())
board = [[0]*col for _ in range(row)]
for _ in range(N):
    y1, x1, y2, x2 = map(int, input().split())
    for y in range(x1, x2):
        for x in range(y1, y2):
            board[y][x] = 1

result = []

visited = [[0]*col for _ in range(row)]
for i in range(row):
    for j in range(col):
        if not visited[i][j] and not board[i][j]:
            visited[i][j] = 1
            q = [[i, j]]
            cnt = 1

            while q:
                y, x = q.pop()

                for dy, dx in ((-1, 0), (0, 1), (0, -1), (1, 0)):
                    newY, newX = y+dy, x+dx
                    if 0 <= newY < row and 0 <= newX < col:
                        if not board[newY][newX] and not visited[newY][newX]:
                            visited[newY][newX] = 1
                            cnt += 1
                            q.append([newY, newX])
            result.append(cnt)

print(len(result))
print(*sorted(result))