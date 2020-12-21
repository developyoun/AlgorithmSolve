def solve(n, arr):
    if n > N: return
    if len(arr) == M:
        answer.append(arr)
        return

    for k in range(n, N+1):
        solve(k, arr + [k])


N, M = map(int, input().split())
answer = []
solve(1, [])
for a in answer:
    print(*a)