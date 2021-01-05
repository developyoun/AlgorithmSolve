N = int(input())
arr = list(map(int, input().split()))
dp = [float('INF')]*N
dp[0] = 0

for i in range(N):
  for j in range(1, arr[i]+1):
    if i+j < N:
      dp[i+j] = min(dp[i]+1, dp[i+j])

result = dp[N-1]
print(-1 if result == float('inf') else result )