from heapq import heappop, heappush
from collections import deque

def getGuest(Y, X):
    hq = []
    heappush(hq, [0, Y, X])
    visited = [[False]*N for _ in range(N)]
    visited[Y][X] = True

    while hq:
        distance, y, x = heappop(hq)

        if board[y][x] < 0:
            number, board[y][x] = -board[y][x], 0
            return distance, number, y, x

        for dy, dx in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < N and 0 <= newX < N and board[newY][newX] != 1 and not visited[newY][newX]:
                visited[newY][newX] = True
                heappush(hq, [distance+1, newY, newX])
    return False

def goDestination(Y, X, goal):
    table = [[-1]*N for _ in range(N)]
    table[Y][X] = 0
    dq = deque()
    dq.append([Y, X])

    while dq:
        y, x = dq.popleft()

        if [y, x] == goal:
            return table[y][x], y, x

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < N and 0 <= newX < N and board[newY][newX] != 1 and table[newY][newX] == -1:
                table[newY][newX] = table[y][x] + 1
                dq.append([newY, newX])
    return False


N, M, e = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
R, C = map(lambda x: int(x)-1, input().split())

info = dict()
for m in range(1, M+1):
    sy, sx, ey, ex = map(lambda x: int(x)-1, input().split())
    board[sy][sx] = -m
    info[m] = [ey, ex]

for _ in range(M):
    items = getGuest(R, C)
    if not items: e = -1; break
    dis, guestNum, R, C = items
    if dis > e: e = -1; break
    e -= dis
    items = goDestination(R, C, info[guestNum])
    if not items: e = -1; break
    dis, R, C = items
    if dis > e: e = -1; break
    e += dis
print(e)