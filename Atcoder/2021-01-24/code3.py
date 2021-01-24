N = int(input())
arr = list(map(int, input().split()))

result = 0

for l in range(N):
    Min = arr[l]
    for r in range(l, N):
        Min = min(Min, arr[r])
        result = max(result, (r-l+1) * Min)

print(result)