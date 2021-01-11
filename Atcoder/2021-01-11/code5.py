N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
roads = [[] for _ in range(N+1)]
answer = [float('INF')] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    roads[s].append(e)
    answer[e] = min(answer[e], arr[s])

for i in range(1, N+1):
    for j in roads[i]:
        answer[j] = min(answer[j], answer[i])

result = -float('INF')
for i in range(1, N+1):
    result = max(result, arr[i]-answer[i])

print(result)