N = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(N-1, 0, -1):
    if arr[i] < arr[i-1]:
        for j in range(N-1, i-1, -1):
            if arr[i-1] > arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                result = arr[:i] + sorted(arr[i:], reverse=True)
                break
        break

if result:
    print(*result)
else:
    print(-1)
