def solve(n, arr):
    if n > N: return
    if len(arr) == M:
        print(*arr)
        return

    for k in range(n, N):
        if not arr or (arr and arr[-1] <= numbers[k]):
            solve(n, arr + [numbers[k]])

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
answer = []
solve(0, [])