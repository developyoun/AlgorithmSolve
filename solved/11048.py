row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

dp = [[0]*col for _ in range(row)]
dp[0][0] = board[0][0]

for i in range(1, col):
    dp[0][i] = board[0][i] + dp[0][i-1]
for i in range(1, row):
    dp[i][0] = board[i][0] + dp[i-1][0]

for i in range(1, row):
    for j in range(1, col):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + board[i][j]

print(dp[row-1][col-1])