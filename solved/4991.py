from collections import deque
from itertools import permutations

def init():
    y, x, dust = -1, -1, []
    for i in range(row):
        for j in range(col):
            if board[i][j] == 'o':
                y, x = i, j 
            elif board[i][j] == '*':
                dust.append([i, j])
    return y, x, dust

def move(sy, sx, ey, ex):
    visited = [[-1] * col for _ in range(row)]
    visited[sy][sx] = 0
    queue = deque()
    queue.append([sy, sx])

    while queue:
        y, x = queue.popleft()
        if [y, x] == [ey, ex]:
            return visited[y][x]

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if not 0 <= new_y < row or not 0 <= new_x < col: continue
            if board[new_y][new_x] == 'x' or visited[new_y][new_x] != -1: continue
            visited[new_y][new_x] = visited[y][x] + 1
            queue.append([new_y, new_x])

    return 0


while True:
    col, row = map(int, input().split())
    if [row, col] == [0, 0]: break
    board = [list(input()) for _ in range(row)]

    init_y, init_x, dusts = init()
    numOfDust = len(dusts)

    initArr = [] * numOfDust
    distanceArr = [[0] * numOfDust for _ in range(numOfDust)]

    for target_y, target_x in dusts:
        initArr.append(move(init_y, init_x, target_y, target_x))

    for i in range(numOfDust):
        for j in range(i+1, numOfDust):
            start_y, start_x = dusts[i]
            goal_y, goal_x = dusts[j]
            distance = move(start_y, start_x, goal_y, goal_x)
            distanceArr[i][j] = distance
            distanceArr[j][i] = distance

    result = float('INF')
    for perm in permutations([i for i in range(numOfDust)], numOfDust):
        now = perm[0]
        if not initArr[now]:
            continue
        total = initArr[now]
        for nxt in perm[1:]:
            if not distanceArr[now][nxt]: break
            total += distanceArr[now][nxt]
            now = nxt
        else:
            result = min(result, total)
    print(-1 if result == float('INF') else result)