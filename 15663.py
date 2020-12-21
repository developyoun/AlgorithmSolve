from itertools import permutations
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

S = set()
for perm in permutations(numbers, M):
    S.add(perm)
for arr in sorted(list(S)):
    print(*arr)