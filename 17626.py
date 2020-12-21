N = int(input())
dp = [4] * (N+1)
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    if int(i**0.5) == i**0.5:
        dp[i] = 1
    else:
        for j in range(1, int(i**0.5)+1):
            dp[i] = min(dp[i], dp[j*j]+dp[i-j*j])
print(dp[N])