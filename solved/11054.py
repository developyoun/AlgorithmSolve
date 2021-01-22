N = int(input())
arr = list(map(int, input().split()))
dp = [[1, 1] for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            dp[j][0] = max(dp[j][0], dp[i][0]+1)
    
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            dp[j][1] = max(dp[j][1], dp[i][0]+1, dp[i][1]+1)

print(max(map(max, dp)))