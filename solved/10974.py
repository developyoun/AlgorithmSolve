from itertools import permutations
N = int(input())
arr = [i for i in range(1, N+1)]

for perm in permutations(arr, N):
    print(*perm)