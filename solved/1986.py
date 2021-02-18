dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
ddy = [-2, -1, 1, 2, 2, 1, -1, -2]
ddx = [1, 2, 2, 1, -1, -2, -2, -1]


N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]

Q = list(map(int, input().split()))
q = []
for i in range(1, len(Q)-1, 2):
    y, x = Q[i]-1, Q[i+1]-1
    board[y][x] = 1
    q.append([y, x])

K = list(map(int, input().split()))
k = []
for i in range(1, len(K)-1, 2):
    y, x = K[i]-1, K[i+1]-1
    board[y][x] = 2
    k.append([y, x])

P = list(map(int, input().split()))
for i in range(1, len(P)-1, 2):
    y, x = P[i]-1, P[i+1]-1
    board[y][x] = 3

for y, x in q:
    for d in range(8):
        newY, newX = y+dy[d], x+dx[d]
        while 0 <= newY < N and 0 <= newX < M and board[newY][newX] <= 0:
            board[newY][newX] = -1
            newY += dy[d]; newX += dx[d]

for y, x in k:
    for d in range(8):
        newY, newX = y+ddy[d], x+ddx[d]
        if 0 <= newY < N and 0 <= newX < M and not board[newY][newX]:
            board[newY][newX] = -1

result = 0
for a in board:
    result += a.count(0)
print(result)
