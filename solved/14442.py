from collections import deque

row, col, k = map(int, input().split())
board = [input() for _ in range(row)]
visited = [[[-1]*(k+1) for _ in range(col)] for _ in range(row)]

visited[0][0][k] = 0
queue = deque()
queue.append([0, 0, k])

while queue:
    y, x, chance = queue.popleft()

    if [y, x] == [row-1, col-1]:
        break

    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_y, new_x = y+dy, x+dx
        if 0 <= new_y < row and 0 <= new_x < col:

            if board[new_y][new_x] == '0' and visited[new_y][new_x][chance] == -1:
                visited[new_y][new_x][chance] = visited[y][x][chance] + 1
                queue.append([new_y, new_x, chance])
            elif board[new_y][new_x] == '1' and chance > 0 and -1 == visited[new_y][new_x][chance-1]:
                visited[new_y][new_x][chance-1] = visited[y][x][chance] + 1
                queue.append([new_y, new_x, chance-1])

result = max(visited[row-1][col-1])+1
print(result if result else -1)
