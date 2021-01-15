from itertools import combinations
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for p in combinations(arr, M):
    print(*p)