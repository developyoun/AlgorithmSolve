row, col = map(int, input().split())
board = [input() for _ in range(row)]
dp = [[0]*col for _ in range(row)]

for r in range(row):
    for c in range(col):
        if not (r and c):
            if board[r][c] == '1':
                dp[r][c] = 1

        elif board[r][c] == '1':
            if dp[r][c-1] == dp[r-1][c] == dp[r-1][c-1]:
                dp[r][c] = dp[r-1][c-1] + 1
            elif dp[r][c-1] and dp[r-1][c] and dp[r-1][c-1]:
                dp[r][c] = min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1])+1
            else:
                dp[r][c] = 1

print(max(map(max, dp))**2)
