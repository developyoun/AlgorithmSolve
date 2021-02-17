N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if not dp[i][j] or not board[i][j]: continue

        num = board[i][j]
        for dy, dx in ((0, 1), (1, 0)):
            newY, newX = i+dy*num, j+dx*num
            if 0 <= newY < N and 0 <= newX < N:
                dp[newY][newX] += dp[i][j]

print(dp[N-1][N-1])