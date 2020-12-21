N = int(input())
board = [input() for _ in range(N)]
visited = [[False]*N for _ in range(N)]

answer = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and not visited[i][j]:
            cnt = 1
            q = [[i, j]]
            visited[i][j] = True
            while q:
                y, x = q.pop()
                for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    new_y, new_x = y+dy, x+dx
                    if 0 <= new_y < N and 0 <= new_x < N:
                        if not visited[new_y][new_x] and board[new_y][new_x] == '1':
                            q.append([new_y, new_x])
                            visited[new_y][new_x] = True
                            cnt += 1
            answer.append(cnt)

print(len(answer))
if len(answer):
    print('\n'.join(map(str, sorted(answer))))