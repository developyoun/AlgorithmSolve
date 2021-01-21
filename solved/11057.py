mod = 10007
dp = [[0]*10 for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, 1001):
    dp[i][0] = 1
    for j in range(1, 10):
        dp[i][j] = (dp[i-1][j]+dp[i][j-1]) % mod

print(sum(dp[int(input())])%mod)