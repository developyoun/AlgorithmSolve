N, K = map(int, input().split())
tmp = sorted([int(input()) for _ in range(N)])

arr = []
for i in range(N-1):
    arr.append(tmp[i+1] - tmp[i])

left, right = 0, max(arr)

while left <= right:
    mid = (left+right)//2

    cnt = 0
    for a in arr:
        if a > mid:
            cnt += 1

    if cnt > K-1:
        right = mid-1
    else:
        left = mid+1

print(right, left)