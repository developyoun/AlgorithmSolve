import sys
from itertools import combinations
from collections import deque, defaultdict

input = sys.stdin.readline

def spread(green, red):
    cnt = 0
    table = [['']*col for _ in range(row)]
    queue = deque()

    for y, x in green:
        table[y][x] = 'G'
        queue.append([y, x])
    for y, x in red:
        table[y][x] = 'R'
        queue.append([y, x])

    while queue:
        save = defaultdict(set)
        for _ in range(len(queue)):
            y, x = queue.popleft()

            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                newY, newX = y+dy, x+dx
                if 0 <= newY < row and 0 <= newX < col:
                    if board[newY][newX] and not table[newY][newX]:
                        save[(newY, newX)].add(table[y][x])
    
        for key, value in save.items():
            y, x = key
            if len(value) == 2:
                cnt += 1
                table[y][x] = 'F'
            else:
                table[y][x] = value.pop()
                queue.append([y, x])
    return cnt

row, col, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

earth = []
for i in range(row):
    for j in range(col):
        if board[i][j] == 2: earth.append((i, j))

result = 0
for comb in combinations(earth, G+R):
    whole = set(comb)
    for g in combinations(comb, G):
        r = tuple(whole - set(g))
        res = spread(g, r)
        result = max(result, res)
print(result)