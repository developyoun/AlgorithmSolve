from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(Y, X, targetY, targetX):
    check = [[-1]*col for _ in range(row)]
    check[Y][X] = 0
    
    queue = deque()
    queue.append([Y, X])

    while queue:
        y, x = queue.popleft()

        if [y, x] == [targetY, targetX]:
            return check[y][x]

        for d in range(4):
            newY, newX = y+dy[d], x+dx[d]
            if 0 <= newY < row and 0 <= newX < col:
                if check[newY][newX] == -1 and board[newY][newX] != '#':
                    check[newY][newX] = check[y][x] + 1
                    queue.append([newY, newX])


result = float('INF')
def dfs(distance, depth, nowY, nowX):
    global result
    if distance > result:
        return
    
    if depth == l:
        newD = dic[(nowY, nowX, ey, ex)]
        result = min(result, distance + newD)
        return

    for k in range(l):
        if visited[k]: continue

        visited[k] = True
        ny, nx = items[k]
        newDistance = dic[(nowY, nowX, ny, nx)]
        dfs(distance+newDistance, depth+1, ny, nx)
        visited[k] = False


col, row = map(int, input().split())
board = [input() for _ in range(row)]

sy, sx = -1, -1
ey, ex = -1, -1
items = []
for i in range(row):
    for j in range(col):
        if board[i][j] == 'S': sy, sx = i, j
        elif board[i][j] == 'X': items.append([i, j])
        elif board[i][j] == 'E': ey, ex = i, j 

l = len(items)
dic = dict()
for i in range(l):
    y1, x1 = items[i]
    dic[(y1, x1, ey, ex)] = bfs(y1, x1, ey, ex)
    for j in range(i+1, l):
        y2, x2 = items[j]
        distance = bfs(y1, x1, y2, x2)
        dic[(y1, x1, y2, x2)] = distance
        dic[(y2, x2, y1, x1)] = distance

if not l:
    result = min(result, bfs(sy, sx, ey, ex))

visited = [False]*l
for i in range(l):
    yy, xx = items[i]
    initDistance = bfs(sy, sx, yy, xx)

    visited[i] = True
    dfs(initDistance, 1, yy, xx)
    visited[i] = False
print(result)