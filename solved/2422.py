from itertools import combinations

N, M = map(int, input().split())

board = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = True
    board[b][a] = True

result = 0
for comb in combinations([i for i in range(1, N+1)], 3):
    a, b, c = comb
    if not (board[a][b] or board[a][c] or board[b][c]):
        result += 1
print(result)