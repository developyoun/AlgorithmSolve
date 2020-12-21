N = int(input())
numbers = list(map(int, input().split()))
left, right = 0, N-1

answer = float('INF')
result = [-1, -1]
while left < right:
    val = abs(numbers[right] + numbers[left])
    right2left = numbers[right] + numbers[left]

    if answer > val:
        answer = val
        result = [numbers[left], numbers[right]]

    if right2left > 0:
        right -= 1
    elif right2left < 0:
        left += 1
    else:
        break
print(*result)