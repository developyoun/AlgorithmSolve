N = int(input())
arr = list(map(int, input().split()))
result = [k for k in arr]

for i in range(N):
    for j in range(i+1, N):
        if arr[i] < arr[j]:
            result[j] = max(result[j], result[i]+arr[j])

print(max(result))