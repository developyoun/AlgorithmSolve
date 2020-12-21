N = int(input())
board = [input() for _ in range(N)]

val1, val2 = 0, 0

visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = board[i][j]
            visited[i][j] = True
            val1 += 1

            q = [[i, j]]
            while q:
                y, x = q.pop()
                for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_y, new_x = y+dy, x+dx
                    if not 0 <= new_y < N or not 0 <= new_x < N: continue
                    if visited[new_y][new_x] or board[new_y][new_x] != color: continue
                    visited[new_y][new_x] = True
                    q.append([new_y, new_x])

visited = [[False]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            color = board[i][j]
            visited[i][j] = True
            val2 += 1

            q = [[i, j]]
            while q:
                y, x = q.pop()
                for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_y, new_x = y+dy, x+dx
                    if not 0 <= new_y < N or not 0 <= new_x < N: continue
                    if visited[new_y][new_x]: continue
                    if (color == board[new_y][new_x]) or (color in 'GR' and board[new_y][new_x] in 'GR'):   
                        visited[new_y][new_x] = True
                        q.append([new_y, new_x])
print(val1, val2)