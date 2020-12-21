N, goal = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 1, max(numbers)

while left <= right:
    mid = (left + right)//2

    cnt = 0
    for num in numbers:
        if num > mid: cnt += num - mid
    
    if cnt >= goal:
        left = mid+1
    else:
        right = mid-1
print(right)