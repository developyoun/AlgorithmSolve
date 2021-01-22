mod = 1000000000
N, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][1] = 1

for i in range(2, K+1):
    dp[0][i] = 1
    for j in range(1, N+1):
        dp[j][i] = (dp[j-1][i] + dp[j][i-1]) % mod

print(dp[N][K])