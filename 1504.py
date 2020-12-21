import sys
from collections import deque
input = sys.stdin.readline
inf = float('INF')

V, E = map(int, input().split())
info = [[inf]*(V+1) for _ in range(V+1)]

for _ in range(E):
    s, e, v = map(int, input().split())
    info[s][e] = min(v, info[s][e])
    info[e][s] = min(v, info[e][s])

a, b = map(int, input().split())
visited = [[[inf for  _ in range(2)] for _ in range(2)] for _ in range(V+1)]

aa = 1 if a == 1 else 0
bb = 1 if b == 1 else 0

visited[1][aa][bb] = 0
queue = deque()
queue.append([1, aa, bb])

while queue:
    now, A, B = queue.popleft()

    for new in range(1, V+1):
        if new == now: continue
        if info[now][new] == inf: continue

        flag_a, flag_b = A, B
        if new == a: flag_a = 1
        if new == b: flag_b = 1

        if visited[new][flag_a][flag_b] > visited[now][A][B] + info[now][new]:
            visited[new][flag_a][flag_b] = visited[now][A][B] + info[now][new]
            queue.append([new, flag_a, flag_b])

result = visited[V][1][1]
print(-1 if result == inf else result)