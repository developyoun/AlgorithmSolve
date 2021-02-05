N, K = map(int, input().split())
dp = [0]*(K+1)
dp[0] = 1

for _ in range(N):
    n = int(input())
    for i in range(K-n+1):
        if i + n <= K and dp[i]:
            dp[i+n] += dp[i]
print(dp[K])