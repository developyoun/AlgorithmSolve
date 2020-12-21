N, target = map(int, input().split())
lines = [int(input()) for _ in range(N)]

left, right = 1, max(lines)
answer = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for line in lines:
        cnt += line // mid
    
    if cnt >= target:
        left = mid+1
        answer = mid
    else:
        right = mid-1
        
print(answer)