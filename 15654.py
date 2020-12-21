from itertools import permutations
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

for perm in permutations(numbers, M):
    print(*perm)