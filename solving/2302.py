N = int(input())
M = int(input())
sit = [int(input()) for _ in range(M)] + [N+1]

result = 1
dp = [0] * (N+1)
dp[1], dp[2] = 1, 2
for n in range(3, N+1):
    dp[n] = dp[n-1] + dp[n-2]

start = 1
for m in sit:
    if m-start:
        result *= dp[m - start]
    start = m+1

print(result)