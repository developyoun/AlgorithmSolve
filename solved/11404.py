N = int(input())
board = [[float('INF')]*(N+1) for _ in range(N+1)]
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    board[a][b] = min(board[a][b], c)

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: board[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            board[i][j] = min(board[i][j], board[i][k]+board[k][j])
for a in board[1:]:
    print(' '.join(map(str, a[1:])).replace('inf', '0'))