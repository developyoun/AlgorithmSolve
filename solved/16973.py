from collections import deque
import sys
input = sys.stdin.readline

def checkedBlock(y, x):
    for r in range(y, y+recHeight):
        if board[r][x]: return False
        if board[r][x+recWidth-1]: return False
    for c in range(x, x+recWidth):
        if board[y][c]: return False
        if board[y+recHeight-1][c]: return False

    return True

def solve(init_y, init_x, goal_y, goal_x):
    visited = [[-1] * col for _ in range(row)]
    visited[init_y][init_x] = 0
    queue = deque()
    queue.append([init_y, init_x])

    while queue:
        y, x = queue.popleft()

        if [y, x] == [goal_y, goal_x]:
            return visited[y][x]

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < row and 0 <= new_y + recHeight <= row and 0 <= new_x < col and 0 <= new_x + recWidth <= col:
                if visited[new_y][new_x] == -1 and checkedBlock(new_y, new_x):
                    visited[new_y][new_x] = visited[y][x] + 1
                    queue.append([new_y, new_x])
    return -1

row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

recHeight, recWidth, sy, sx, ey, ex = map(int, input().split())
print(solve(sy-1, sx-1, ey-1, ex-1))