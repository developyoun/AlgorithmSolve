def solve(depth, result, idx):
    
    if depth == M:
        answer.add(tuple(result))
        return
    
    for n in range(idx+1, N):
        if not visited[n] and result[-1] <= arr[n]:
            visited[n] = 1
            solve(depth+1, result + [arr[n]], n)
            visited[n] = 0

answer = set()
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [0] * N

for i in range(N):
    visited[i] = 1
    solve(1, [arr[i]], i)
    visited[i] = 0

for s in sorted(list(answer)):
    print(*s)