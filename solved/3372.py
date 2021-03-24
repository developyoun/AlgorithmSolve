N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if dp[i][j] and board[i][j]:
            distance = board[i][j]
            if 0 <= i+distance < N: dp[i+distance][j] += dp[i][j]
            if 0 <= j+distance < N: dp[i][j+distance] += dp[i][j]

print(dp[N-1][N-1])
