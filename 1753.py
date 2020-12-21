import sys, heapq
input = sys.stdin.readline
inf = float('INF')

V, E = map(int, input().split())
start = int(input())
info = [[] for _ in range(V+1)]
for _ in range(E):
    s, e, v = map(int, input().split())
    info[s].append([e, v])

heap = []
heapq.heappush(heap, [0, start])
visited = [inf] * (V+1)
visited[start] = 0
while heap:
    val, now = heapq.heappop(heap)
    
    if visited[now] > val:
        continue
    
    for new, dis in info[now]:
        if visited[new] > dis + val:
            visited[new] = dis + val
            heapq.heappush(heap, [dis+val, new])

print('\n'.join(map(str, visited[1:])).replace('inf', 'INF'))    
