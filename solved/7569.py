from collections import deque

col, row, height = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(row)] for _ in range(height)]
visited = [[[False]*col for _ in range(row)] for _ in range(height)]
cnt = 0

queue = deque()
for h in range(height):
    for r in range(row):
        for c in range(col):
            if board[h][r][c] == 1:
                queue.append([h, r, c])
                visited[h][r][c] = True
            elif not board[h][r][c]:
                cnt += 1

result = 0
while queue:

    result += 1
    for _ in range(len(queue)):
        z, y, x = queue.popleft()

        for dz, dy, dx in ((1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1)):
            new_z, new_y, new_x = z+dz, y+dy, x+dx
            if not 0 <= new_z < height or not 0 <= new_y < row or not 0 <= new_x < col: continue
            if not board[new_z][new_y][new_x] and not visited[new_z][new_y][new_x]:
                queue.append([new_z, new_y, new_x])
                visited[new_z][new_y][new_x] = True
                cnt -= 1

print(result-1 if not cnt else -1)