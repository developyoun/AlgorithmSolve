from itertools import permutations
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def calculator(y, x, k, matrix):
    tmp = [[matrix[i][j] for j in range(col)] for i in range(row)]

    i, j = y-k, x-k
    d = 0
    while k:
        move = (k*2)*4
        for _ in range(move):
            if not (y-k <= i+dy[d] <= y+k and x-k <= j+dx[d] <= x+k):
                d = (d+1)%4
            tmp[i+dy[d]][j+dx[d]] = matrix[i][j]
            i, j = i+dy[d], j+dx[d]

        k -= 1
        i, j = y-k, x-k

    return tmp

row, col, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

seq = []
for _ in range(N):
    r, c, s = map(int, input().split())
    seq.append([r-1, c-1, s])


result = float('INF')
for perm in permutations(seq, N):
    matrix = [[board[i][j] for j in range(col)] for i in range(row)]
    for R, C, S in perm:
        matrix = calculator(R, C, S, matrix)

    for m in matrix:
        result = min(sum(m), result)
print(result)