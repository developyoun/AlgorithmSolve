from itertools import combinations
from collections import deque

def calcDistance(nowY, nowX, newMap):
    visited = [[0]*col for _ in range(row)]

    visited[nowY][nowX] = 1
    dq = deque()
    dq.append([nowY, nowX])

    while dq:
        y, x = dq.popleft()

        if visited[y][x] > D: 
            break
        if newMap[y][x]:
            return y, x

        for dy, dx in ((0, -1), (-1, 0), (0, 1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < row and 0 <= newX < col and not visited[newY][newX]:
                visited[newY][newX] = visited[y][x] + 1
                dq.append([newY, newX])
    return -1, -1


def attack(archors):
    newMap = [[board[i][j] for j in range(col)] for i in range(row)]

    cnt = 0
    for y in range(row-1, -1, -1):

        pos = set()
        for archor in archors:
            resY, resX = calcDistance(y, archor, newMap)
            if resY == -1 or resX == -1: continue
            pos.add((resY, resX))

        for delY, delX in pos:
            newMap[delY][delX] = 0
            cnt += 1
    return cnt


row, col, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

result = 0
for comb in combinations(range(col), 3):
    result = max(result, attack(comb))
print(result)