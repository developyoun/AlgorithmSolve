from heapq import heappop, heappush
inf = float('INF')

def solve(arr):
    visited = [inf] * (N+1)
    visited[X] = 0
    heap = [[0, X]]

    while heap:
        now_distance, now_node = heappop(heap)

        for new_node, add_distance in arr[now_node]:
            if visited[new_node] > now_distance + add_distance:
                visited[new_node] = now_distance + add_distance
                heappush(heap, [now_distance + add_distance, new_node]) 
    return visited

N, M, X = map(int, input().split())
info1 = [[] for _ in range(N+1)]
info2 = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, v = map(int, input().split())
    info1[s].append([e, v])
    info2[e].append([s, v])

target2host = solve(info1)
host2target = solve(info2)

result = 0
for i in range(1, N+1):
    result = max(result, host2target[i] + target2host[i])
print(result)