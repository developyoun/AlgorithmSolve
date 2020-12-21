def solve(idx, arr):
    
    if len(arr) == M:
        S.add(tuple(arr))
        return

    for i in range(idx, N):
        if not arr or (arr and arr[-1] <= numbers[i]):
            solve(idx, arr + [numbers[i]])

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

S = set()
solve(0, [])

for a in sorted(list(S)):
    print(*a)