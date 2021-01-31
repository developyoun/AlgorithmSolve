import sys
input = sys.stdin.readline
from collections import deque
inf = float('INF')

def move(N):
    visited = [[inf]*N for _ in range(N)]
    visited[0][0] = board[0][0]
    queue = deque()
    queue.append([0, 0, board[0][0]])

    while queue:
        y, x, v = queue.popleft()
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < N and 0 <= newX < N and visited[newY][newX] > v + board[newY][newX]:
                newV = v + board[newY][newX]
                visited[newY][newX] = newV
                queue.append([newY, newX, newV])
    return visited[N-1][N-1]


case = 1
while True:
    N = int(input())
    if not N: break
    board = [list(map(int, input().split())) for _ in range(N)]

    print('Problem {}: {}'.format(case, move(N)))
    case += 1