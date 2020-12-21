from collections import deque

row, col = map(int, input().split())
board = [input() for _ in range(row)]
values = [[0]*col for _ in range(row)]

values[0][0] = 1

q = deque()
q.append([0, 0])

while q:
    y, x = q.popleft()

    if [y, x] == [row-1, col-1]:
        break

    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_y, new_x = y+dy, x+dx

        if 0 <= new_y < row and 0 <= new_x < col and board[new_y][new_x] == '1' and not values[new_y][new_x]:
            values[new_y][new_x] = values[y][x] + 1
            q.append([new_y, new_x])

print(values[row-1][col-1])