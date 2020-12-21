N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
result = [[0]*(N*K) for _ in range(N*K)]

for i in range(N):
    for j in range(N):
        if board[i][j]:
            for r in range(i*K, i*K+K):
                for c in range(j*K, j*K+K):
                    result[r][c] = 1
for r in result:
    print(' '.join(map(str, r)))