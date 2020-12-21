import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sum_board = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        sum_board[i][j] = board[i-1][j-1] + sum_board[i-1][j] + sum_board[i][j-1] - sum_board[i-1][j-1]

answer = []
for __ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    result = sum_board[y2][x2] - sum_board[y2][x1-1] - sum_board[y1-1][x2] + sum_board[y1-1][x1-1]
    answer.append(result)
print('\n'.join(map(str, answer)))