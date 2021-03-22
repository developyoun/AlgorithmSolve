from collections import deque
from itertools import permutations

def solve(matrix):
    visited = [[[-1]*5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = 0
    queue = deque()
    queue.append([0, 0, 0])
    
    while queue:
        z, y, x = queue.popleft()

        for dz, dy, dx in ((-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1)):
            new_z, new_y, new_x = z+dz, y+dy, x+dx
            if 0 <= new_z < 5 and 0 <= new_y < 5 and 0 <= new_x < 5:
                if matrix[new_z][new_y][new_x] and visited[new_z][new_y][new_x] == -1:
                    visited[new_z][new_y][new_x] = visited[z][y][x] + 1
                    queue.append([new_z, new_y, new_x])
    
    val = visited[4][4][4]
    return (False, -1) if val == -1 else (True, val)


def rotate(matrix):
    new_matrix = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new_matrix[j][4-i] = matrix[i][j]
    return new_matrix


def make_maze(floor, arr):
    global result
    if floor == 5:
        if not arr[4][4][4]: 
            return
        flag, value = solve(arr)
        if flag: result = min(result, value)
        return
    
    if floor >= 1 and not arr[0][0][0]:
        return

    idx = perm[floor]
    table = board[idx]
    for _ in range(4):
        table = rotate(table)
        make_maze(floor+1, arr + [table])

board = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
MAX = float('INF')
result = MAX

for perm in permutations(range(5), 5):
    make_maze(0, [])

print(-1 if result == MAX else result)