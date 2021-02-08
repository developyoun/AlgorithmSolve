row, col = map(int, input().split())
paperNum = int(input())

arr = []
left, right = 1, 1000001
M = int(input())
for _ in range(M):
    r, c = map(int, input().split())
    arr.append(c)
    left = max(left, r)

arr.sort()
result = 0
while left <= right:
    mid = (left+right) // 2

    std, cnt = arr[0], 1
    for i in range(1, M):
        x = arr[i]
        if x >= (mid + std):
            std = x
            cnt += 1

    if cnt <= paperNum:
        right = mid-1
        result = mid
    else:
        left = mid+1
print(result)