from itertools import combinations

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

home, store = [], []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            home.append([i, j])
        elif board[i][j] == 2:
            store.append([i, j])

result = float('INF')
for comb in combinations(store, K):
    tmp_result = 0
    for y, x in home:
        tmp = float('INF')
        for cy, cx in comb:
            tmp = min(tmp, abs(cy-y)+abs(cx-x))
        tmp_result += tmp
    result = min(result, tmp_result)
print(result)