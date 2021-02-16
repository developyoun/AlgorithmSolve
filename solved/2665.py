from collections import deque
inf = float('INF')

N = int(input())
board = [input() for _ in range(N)]

init = 1 if board[0][0] == '0' else 0

visited = [[inf]*N for _ in range(N)]
visited[0][0] = init

queue = deque()
queue.append([0, 0, init])

while queue:
    y, x, m = queue.popleft()

    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        newY, newX = y+dy, x+dx
        if 0 <= newY < N and 0 <= newX < N:
            if board[newY][newX] == '1' and visited[newY][newX] > m:
                queue.append([newY, newX, m])
                visited[newY][newX] = m
            elif board[newY][newX] == '0' and visited[newY][newX] > m+1:
                queue.append([newY, newX, m+1])
                visited[newY][newX] = m+1

print(visited[N-1][N-1])