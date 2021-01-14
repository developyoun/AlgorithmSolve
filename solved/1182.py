from itertools import combinations

N, s = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for n in range(1, N+1):
    for comb in combinations(arr, n):
        if sum(comb) == s: result += 1

print(result)