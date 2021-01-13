from collections import deque
direct = ([-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1])
def solve():
    visited = [[[0]*(k+1) for _ in range(col)] for _ in range(row)]
    visited[0][0][k] = 1
    queue = deque()
    queue.append([0, 0, k])

    while queue:
        y, x, jump = queue.popleft()

        if [y, x] == [row-1, col-1]:
            return visited[y][x][jump]-1

        if jump:
            for dy, dx in direct:
                new_y, new_x = y+dy, x+dx
                if 0 <= new_y < row and 0 <= new_x < col:
                    if not board[new_y][new_x] and not visited[new_y][new_x][jump-1]:
                        visited[new_y][new_x][jump-1] = visited[y][x][jump] + 1
                        queue.append([new_y, new_x, jump-1])

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < row and 0 <= new_x < col:
                if not board[new_y][new_x] and not visited[new_y][new_x][jump]:
                    visited[new_y][new_x][jump] = visited[y][x][jump] + 1
                    queue.append([new_y, new_x, jump])
    return -1

k = int(input())
col, row = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

print(solve())