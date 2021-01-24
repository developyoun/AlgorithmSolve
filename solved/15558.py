from collections import deque

N, K = map(int, input().split())
board = [input() for _ in range(2)]
visited = [[0]*N for _ in range(2)]
visited[0][0] = 1
queue = deque()
queue.append([0, 0])

flag = False
time = 0
while queue:
  
    for _ in range(len(queue)):
        y, x = queue.popleft()
        if flag: break

        for new_y, dx in ((y, 1), (y, -1), (not y, K)):
            new_x = x+dx
            if new_x >= N:
                flag = True
                break
            
            elif time < new_x < N and not visited[new_y][new_x] and board[new_y][new_x] == '1':
                visited[new_y][new_x] = 1
                queue.append([new_y, new_x])
    time += 1

print(1 if flag else 0)