N = int(input())
numbers = [int(input()) for _ in range(N)]

dp = [1]*N
for i in range(N):
    for j in range(i+1, N):
        if numbers[i] < numbers[j]:
            dp[j] = max(dp[j], dp[i]+1)
print(N-max(dp))