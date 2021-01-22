N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
idx_arr = [-1] * N

for i in range(N):
    for j in range(i+1, N):
        if arr[i] < arr[j] and dp[j] < dp[i]+1:
            dp[j] = dp[i]+1
            idx_arr[j] = i

answer = max(dp)
idx = dp.index(answer)

result = []
while True:
    result.append(arr[idx])
    idx = idx_arr[idx]
    if idx == -1:
        break
print(answer)
print(*result[::-1])