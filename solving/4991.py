from collections import deque
from heapq import heappush, heappop

def init():
    arr = []
    Y, X = 0, 0
    for i in range(row):
        for j in range(col):
            if board[i][j] == '*':
                arr.append([i, j])
            elif board[i][j] == 'o': 
                Y, X = i, j
                board[i][j] = '.'
    return Y, X, arr


def search_dust(start, end):
    sy, sx = start
    ey, ex = end

    visited = [[-1]*col for _ in range(row)]
    visited[sy][sx] = 0
    queue = deque()
    queue.append([sy, sx])

    while queue:
        y, x = queue.popleft()
        if [y, x] == [ey, ex]:
            return visited[y][x]

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < row and 0 <= new_x < col and visited[new_y][new_x] == -1 and board[new_y][new_x] != 'x':
                visited[new_y][new_x] = visited[y][x]+1
                queue.append([new_y, new_x])

    return -1, -1, -1


while True:
    col, row = map(int, input().split())
    if [row, col] == [0, 0]: break

    board = [list(input()) for _ in range(row)]

    r, c, dust = init()
    heap, tmp = [], []
    result = 0

    for n in range(len(dust)):
        distance = search_dust([r, c], dust[n])
        tmp.append(distance)

    for n in range(len(dust)):
        for m in range(len(dust)):
            if n == m: continue
            distance = search_dust(dust[n], dust[m])
            if distance == -1: continue
            heappush(heap, [distance, n, m])
    print(heap)