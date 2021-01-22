N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]
if N == 1:
    print(arr[0])
else:
    dp[0][0] = arr[0]
    dp[1][0], dp[1][1] = max(arr[1], arr[0]), arr[1] + arr[0]

    for i in range(2, N):
        dp[i][0] = dp[i-2][1] + arr[i]
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]+arr[i])
    print(max(dp[N-1]))