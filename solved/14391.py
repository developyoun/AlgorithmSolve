def solve(total):
    
    global result
    result = max(result, total)

    for i in range(row):
        for j in range(col):
            if visited[i][j]: continue

            visited[i][j] = 1
            solve(total+board[i][j])
            visited[i][j] = 0

            visited[i][j] = 1
            idx, val = 1, board[i][j]
            while j+idx < col and not visited[i][j+idx]:
                visited[i][j+idx] = 1
                val = val*10 + board[i][j+idx]
                solve(total + val)
                idx += 1
            while idx - 1:
                visited[i][j+idx-1] = 0
                idx -= 1

            idx, val = 1, board[i][j]
            while i+idx < row and not visited[i+idx][j]:
                visited[i+idx][j] = 1
                val = val*10 + board[i+idx][j]
                solve(total + val)
                idx += 1
            while idx - 1:
                visited[i+idx-1][j] = 0
                idx -= 1
            visited[i][j] = 0

            return 

row, col = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(row)]

visited = [[0]*col for _ in range(row)]
result = 0
solve(0)
print(result)