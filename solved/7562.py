from collections import deque

case = int(input())

def solve(r, c):
    visited = [[-1]*N for _ in range(N)]
    visited[r][c] = 0
    queue = deque()
    queue.append([r, c])

    while queue:
        y, x = queue.popleft()

        if [y, x] == [yy, xx]:
            return visited[y][x]

        for dy, dx in ((2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < N and 0 <= new_x < N and visited[new_y][new_x] == -1:
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append([new_y, new_x]) 
    return -1


for _ in range(case):
    N = int(input())
    yy, xx = map(int, input().split())
    i, j = map(int, input().split())

    print(solve(i, j))
