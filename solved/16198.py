from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))

result = 0
for perm in permutations([i for i in range(1, N-1)], N-2):
    visited = [False] * N

    tmpResult = 0
    for p in perm:
        visited[p] = True
        left, right = p-1, p+1
        while visited[left]: left -= 1
        while visited[right]: right += 1
        tmpResult += arr[left] * arr[right]
    
    result = max(tmpResult, result)

print(result)
