from itertools import permutations
N = int(input())
arr = list(map(int, input().split()))

result = 0
for perm in permutations(arr, N):
    tmp = 0
    for i in range(N-1):
        tmp += abs(perm[i] - perm[i+1])
    result = max(result, tmp)
print(result)