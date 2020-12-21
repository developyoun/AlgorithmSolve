from collections import deque

col, row = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
visited = [[False]*col for _ in range(row)]
cnt = 0

queue = deque()
for r in range(row):
    for c in range(col):
        if board[r][c] == 1:
            queue.append([r, c])
            visited[r][c] = True
        elif not board[r][c]:
            cnt += 1

result = 0
while queue:

    result += 1
    for _ in range(len(queue)):
        y, x = queue.popleft()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if not 0 <= new_y < row or not 0 <= new_x < col: continue
            if not board[new_y][new_x] and not visited[new_y][new_x]:
                queue.append([new_y, new_x])
                visited[new_y][new_x] = True
                cnt -= 1

print(result-1 if not cnt else -1)