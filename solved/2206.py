from collections import deque
inf = float('INF')

row, col = map(int, input().split())
board = [input() for _ in range(row)]
visited = [[[inf, inf] for _ in range(col)] for _ in range(row)]
dq = deque()

visited[0][0][0] = 1
dq.append([0, 0, False])
while dq:
    y, x, flag = dq.popleft()

    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_y, new_x = y+dy, x+dx
        if not 0 <= new_y < row or not 0 <= new_x < col: continue

        if flag:
            if board[new_y][new_x] == '0' and visited[new_y][new_x][1] > visited[y][x][1] + 1:
                visited[new_y][new_x][1] = visited[y][x][1] + 1
                dq.append([new_y, new_x, True])

        else:
            if board[new_y][new_x] == '1':
                if visited[new_y][new_x][1] > visited[y][x][0] + 1:
                    visited[new_y][new_x][1] = visited[y][x][0] + 1
                    dq.append([new_y, new_x, True])
            else:
                if visited[new_y][new_x][0] > visited[y][x][0] + 1:
                    visited[new_y][new_x][0] = visited[y][x][0] + 1
                    dq.append([new_y, new_x, False])
answer = min(visited[row-1][col-1])
print(-1 if answer == float('INF') else answer)