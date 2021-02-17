
dic = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, 1), (0, -1)),
    '+': ((-1, 0), (0, 1), (1, 0), (0, -1)),
    '1': ((0, 1), (1, 0)),
    "2": ((-1, 0), (0, 1)),
    "3": ((-1, 0), (0, -1)),
    "4": ((1, 0), (0, -1))
}

def isConnect(y, x):
    for dy, dx in ((0, 1), (-1, 0), (0, -1), (1, 0)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < row and 0 <= nx < col:
            if board[ny][nx] not in ('M', "Z", "."): return True, ny, nx
    return False, -1, -1

def findShape(y, x):
    s = set()
    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        newY, newX = y+dy, x+dx
        if 0 <= newY < row and 0 <= newX < col and board[newY][newX] != '.':
            if board[newY][newX] == 'M':
                if not connectM: s.add((dy, dx))
            elif board[newY][newX] == 'Z':
                if not connectZ: s.add((dy, dx))
            elif (-dy, -dx) in dic[board[newY][newX]]:
                s.add((dy, dx))

    for key, value in dic.items():
        if not (set(value) - s) and len(value) == len(s):
            return key
    return -1


def solve(Y, X):
    visited[Y][X] = 1
    q = [[Y, X]]
    while q:
        y, x = q.pop()

        shape = board[y][x]
        for dy, dx in dic[shape]:
            newY, newX = y+dy, x+dx
            if board[newY][newX] == '.':
                res = findShape(newY, newX)
                return newY, newX, res

            elif visited[newY][newX]: continue

            else:
                visited[newY][newX] = 1
                q.append([newY, newX])

row, col = map(int, input().split())
board = [input() for _ in range(row)]
visited = [[0]*col for _ in range(row)]

sy, sx = -1, -1
connectM, connectZ = False, False
for i in range(row):
    for j in range(col):
        if board[i][j] == '.': 
            continue
        elif board[i][j] == 'M':
            connectM, yy, xx = isConnect(i, j)
            if connectM: 
                visited[i][j] = True
                sy, sx = yy, xx
        elif board[i][j] == 'Z': 
            connectZ, yy, xx = isConnect(i, j)
            if connectZ: 
                visited[i][j] = True
                sy, sx = yy, xx

r, c, result = solve(sy, sx)
print(r+1, c+1, result)