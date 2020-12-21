def dfs(y):
    global result

    if y == N:
        result += 1
        return
    
    for x in range(N):
        if not (col[x] or left[y+x] or right[y-x]):
            col[x] = left[y+x] = right[y-x] = True
            dfs(y+1)
            col[x] = left[y+x] = right[y-x] = False

N = int(input())
col, right, left = [False] * N, [False] * (2*N+1), [False] * (2*N+1)

result = 0
dfs(0)
print(result)