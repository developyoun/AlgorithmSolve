dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

board = [[0]*101 for _ in range(101)]

N = int(input())
y, x, d = 50, 50, 2
board[y][x] = 1
for D in input():
    if D == 'F':
        newY, newX = y+dy[d], x+dx[d]
        board[newY][newX] = 1
        y, x = newY, newX

    elif D == 'L':
        d = (d-1)%4
    elif D == 'R':
        d = (d+1)%4
minY, minX, maxY, maxX = 101, 101, 0, 0
for i in range(101):
    for j in range(101):
        if board[i][j]:
            minY, minX, maxY, maxX = min(minY, i), min(minX, j), max(maxY, i), max(maxX, j)

for r in range(minY, maxY+1):
    val = ''
    for c in range(minX, maxX+1):
        if board[r][c]: val += '.'
        else: val += '#'
    print(val)
