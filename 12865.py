N, W = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(W+1) for _ in range(N+1)]

for n in range(1, N+1):
    for w in range(1, W+1):
        weight, value = bags[n-1]

        if weight <= w:
            dp[n][w] = max(dp[n-1][w], value + dp[n-1][w-weight])
        else:
            dp[n][w] = dp[n-1][w]

print(dp[N][W])