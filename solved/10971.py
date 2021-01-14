def solve(depth, x, value, arr):
    global result

    if value >= result:
        return

    if depth == N:
        result = min(result, value)
        return

    for c in range(N):
        if board[x][c] and not visited[c] and x != i:
            visited[c] = True
            solve(depth+1, c, value+board[x][c], arr+[c])
            visited[c] = False

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False]*N

result = float('INF')
for i in range(N):
    for j in range(N):
        if not board[i][j]: continue
        visited[j] = True
        solve(1, j, board[i][j], [j])
        visited[j] = False

print(result)