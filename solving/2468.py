def inWater(height):
    visited = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if board[r][c] <= height:
                visited[r][c] = 1
    
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                cnt += 1
                visited[r][c] = 1
                q = [[r, c]]

                while q:
                    y, x = q.pop()
                    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        newY, newX = y+dy, x+dx
                        if 0 <= newY < N and 0 <= newX < N and not visited[newY][newX]:
                            visited[newY][newX] = 1
                            q.append([newY, newX])
    return cnt

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


result = 0
for i in range(101):
    result = max(result, inWater(i))

print(result)