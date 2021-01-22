N = int(input())
arr = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N)]

dp[0][0], dp[0][1] = arr[0], arr[0]
for i in range(1, N):
    dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1]+arr[i])
print(max(map(max, dp)))