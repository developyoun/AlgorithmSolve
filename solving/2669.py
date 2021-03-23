arr = []
for _ in range(4):
    arr.append(list(map(int, input().split())))

board = [[0]*100 for _ in range(100)]
for y1, x1, y2, x2 in arr:
    for i in range(y1-1, y2-1):
        for j in range(x1-1, x2-1):
            board[i][j] += 1

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            cnt += 1
print(cnt)