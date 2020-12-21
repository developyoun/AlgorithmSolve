H, N = map(int, input().split())
visited = [[0]*31 for _ in range(31)]

if H > N:
    for y in range(H, N-1, -1):
        for x in range(H, N-1, -1):
            if x < y: continue
            elif y == H or x == H: visited[y][x] = 1
            else:
                visited[y][x] = visited[y+1][x] + visited[y][x+1]
    print(visited[N][N])
else:
    visited[H][H] = 1
    for y in range(H, N+1):
        for x in range(H, N+1):
            if x < y: continue
            elif y == H or x == H: visited[y][x] = 1
            else:
                visited[y][x] = visited[y-1][x] + visited[y][x-1]
    print(visited[N][N])