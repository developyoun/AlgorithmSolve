from collections import deque
import sys
input = sys.stdin.readline

def init():
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if board[i][j][k] == 'S':
                    return i, j, k

def solve(sl, sy, sx):
    visited = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[sl][sy][sx] = 0
    queue = deque()
    queue.append([sl, sy, sx])

    while queue:
        z, y, x = queue.popleft()

        if board[z][y][x] == 'E':
            return 'Escaped in {} minute(s).'.format(visited[z][y][x])

        for dz, dy, dx in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1)):
            newZ, newY, newX = z+dz, y+dy, x+dx
            if 0 <= newZ < L and 0 <= newY < R and 0 <= newX < C:
                if board[newZ][newY][newX] != '#' and visited[newZ][newY][newX] == -1:
                    queue.append([newZ, newY, newX])
                    visited[newZ][newY][newX] = visited[z][y][x] + 1
    return 'Trapped!'


while True:
    L, R, C = map(int, input().rstrip().split())
    if not (L and R and C): break
    board = []
    
    for _ in range(L):
        board.append([input() for _ in range(R)])
        input()

    l, r, c = init()
    print(solve(l, r, c))