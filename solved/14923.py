"""
미로 탈출

input:
5 6
1 1
5 6
0 1 1 1 0 0
0 1 1 0 0 0
0 1 0 0 1 0
0 1 0 0 1 0
0 0 0 1 1 0
"""
from collections import deque

row, col = map(int, input().split())
init_y, init_x = map(int, input().split())
goal_y, goal_x = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

visited = [[[0]*2 for _ in range(col)] for _ in range(row)] # 안부순 이동거리와 부순 이동거리 저장배열
visited[init_y-1][init_x-1][0] = 1
queue = deque()
# 세번째는 이동거리, 마지막은 벽을 부술 수 있는지 없는지 확인하는 flag
queue.append([init_y-1, init_x-1, 0])  

result = -1
while queue:
    y, x, flag = queue.popleft()

    if [y, x] == [goal_y-1, goal_x-1]: result = visited[y][x][flag]-1; break

    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        new_y, new_x = y+dy, x+dx
        if not 0 <= new_y < row or not 0 <= new_x < col: continue   # 범위 넘어가는 것 방지
        if not board[new_y][new_x] and not visited[new_y][new_x][flag]:
            visited[new_y][new_x][flag] = visited[y][x][flag]+1
            queue.append([new_y, new_x, flag])
        
        elif not flag and board[new_y][new_x] and not visited[new_y][new_x][0]:
            visited[new_y][new_x][1] = visited[y][x][0]+1
            queue.append([new_y, new_x, 1])

print(result)