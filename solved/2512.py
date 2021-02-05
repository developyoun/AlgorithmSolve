N = int(input())
arr = list(map(int, input().split()))
limit = int(input())

left, right = 0, max(arr)
while left <= right:
    mid = (left+right)//2

    total = 0
    for a in arr:
        if a < mid:
            total += a
        else:
            total += mid
    
    if total > limit:
        right = mid-1
    else:
        left = mid+1
print(right)