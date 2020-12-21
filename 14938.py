inf = float('INF')

N, M, K = map(int, input().split())
items = list(map(int, input().split()))

MAP = [[inf for _ in range(N)] for _ in range(N)]
for _ in range(K):
    a, b, c = map(int, input().split())
    MAP[a-1][b-1] = min(MAP[a-1][b-1], c)
    MAP[b-1][a-1] = min(MAP[b-1][a-1], c)

for i in range(N):
    for j in range(N):
        if i == j: MAP[i][j] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            MAP[i][j] = min(MAP[i][j], MAP[i][k] + MAP[k][j])

answer = 0
for r in range(N):
    cnt = 0
    for c in range(N):
        if MAP[r][c] <= M: cnt += items[c]
    answer = max(answer, cnt)
print(answer)