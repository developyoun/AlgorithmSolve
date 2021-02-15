def solve(Y, X):
    stack = [[Y, X]]
    q = [[Y, X]]
    while q:
        y, x = q.pop()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < N and 0 <= newX < N and board[newY][newX] == '#' and not visited[newY][newX]:
                visited[newY][newX] = True
                q.append([newY, newX])
                stack.append([newY, newX])

    res, cnt = len(stack), 0
    while stack:
        y, x = stack.pop()
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if not 0 <= newY < N or not 0 <= newX < N or board[newY][newX] == '.':
                cnt += 1
    return res, cnt


N = int(input())
board = [input() for _ in range(N)]
visited = [[False]*N for _ in range(N)]

result1, result2 = 0, 10**6
for r in range(N):
    for c in range(N):
        if board[r][c] == '#' and not visited[r][c]:
            visited[r][c] = True
            val1, val2 = solve(r, c)
            if result1 < val1:
                result1, result2 = val1, val2
            elif result1 == val1:
                result2 = min(result2, val2)
print(result1, result2)