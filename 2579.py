N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]

dp[0][0] = arr[0]
if N != 1:
    dp[1][0] = arr[1]
    dp[1][1] = arr[0] + arr[1]

for i in range(2, N):
    dp[i][0] = max(dp[i-2]) + arr[i]
    dp[i][1] = dp[i-1][0] + arr[i]

print(max(dp[N-1]))