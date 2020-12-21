import heapq
from collections import deque

def solve():
    heap = []
    heapq.heappush(heap, [0, a])
    dist[a] = 0

    while heap:
        distance, now = heapq.heappop(heap)

        if now == b:
            return

        for new, val in info[now]:
            if dist[new] > distance + val:
                dist[new] = distance + val
                visited[new] = now
                heapq.heappush(heap, [distance+val, new])


inf = float('INF')
V = int(input())
dist  = [inf for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
info = [[] for _ in range(V+1)]
E = int(input())
for _ in range(E):
    s, e, v = map(int, input().split())
    info[s].append([e, v])

a, b = map(int, input().split())
solve()

route = deque()

idx = b
while idx != a:
    route.appendleft(idx)
    idx = visited[idx]
route.appendleft(a)

print(dist[b])
print(len(route))
print(*route)