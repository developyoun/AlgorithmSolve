from heapq import heappop, heappush

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, v = map(int, input().split())
    arr[s].append([v, e])
    arr[e].append([v, s])

result = 0

visited = [False]*(N+1)
q = []
heappush(q, [0, 1])
while q:
    value, node = heappop(q)
    
    if visited[node]: continue
    visited[node] = True
    result += value

    for v, new in arr[node]:
        heappush(q, [v, new])

print(result)