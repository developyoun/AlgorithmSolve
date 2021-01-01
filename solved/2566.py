board = [list(map(int, input().split())) for _ in range(9)]

ans, r, c = 0, 0, 0
for i in range(9):
    for j in range(9):
        if board[i][j] > ans:
            ans, r, c = board[i][j], i, j
print(ans)
print(r+1, c+1)