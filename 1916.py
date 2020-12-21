from heapq import heappop, heappush
inf = float('INF')

def solve(start):
    visited = [inf] * (N+1)
    visited[start] = 0
    heap = [[0, start]]

    while heap:
        now_distance, now_node = heappop(heap)

        if now_node == b:
            return visited[b]

        for new_node, new_distance in info[now_node]:
            total_distance = now_distance + new_distance
            if visited[new_node] > total_distance:
                visited[new_node] = total_distance
                heappush(heap, [total_distance, new_node])


N = int(input())
info = [[] for _ in range(N+1)]
for _ in range(int(input())):
    s, e, v = map(int, input().split())
    info[s].append([e, v])

a, b = map(int, input().split())
result = solve(a)
print(result)