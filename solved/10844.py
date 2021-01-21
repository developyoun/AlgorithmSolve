mod = 1000000000
dp = [[0]*10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1
for i in range(2, 101):
    for j in range(10):
        if j + 1 < 10:
            dp[i][j+1] = (dp[i][j+1] + dp[i-1][j]) % mod
    for j in range(10):
        if 0 <= j - 1:
            dp[i][j-1] = (dp[i][j-1] + dp[i-1][j]) % mod

print(sum(dp[int(input())])%mod)