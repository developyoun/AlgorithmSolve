from collections import deque
MAX = float('INF')

col, row = map(int, input().split())
board = [input() for _ in range(row)]
visited = [[MAX]*col for _ in range(row)]
visited[0][0] = 0
queue = deque()
queue.append([0, 0, 0])

while queue:
    y, x, cnt = queue.popleft()

    if visited[y][x] < cnt:
        continue

    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_y, new_x = y+dy, x+dx
        if not 0 <= new_y < row or not 0 <= new_x < col: continue 
        if board[new_y][new_x] == '1':
            if visited[new_y][new_x] > cnt+1:
                visited[new_y][new_x] = cnt + 1
                queue.append([new_y, new_x, cnt+1])
        else:
            if visited[new_y][new_x] > cnt:
                visited[new_y][new_x] = cnt
                queue.append([new_y, new_x, cnt])

print(visited[row-1][col-1])