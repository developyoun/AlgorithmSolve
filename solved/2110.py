N, K = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

left, right = 1, arr[-1]-arr[0]

result = 0
while left <= right:
    mid = (left+right)//2

    std, cnt = arr[0], 1
    for i in range(1, N):
        if arr[i] - std >= mid:
            cnt += 1
            std = arr[i]

    if cnt < K:
        right = mid-1
    else:
        result = mid
        left = mid+1
print(result)