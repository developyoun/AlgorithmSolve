N = int(input())
target = list(map(int, input().split()))

result = []
for n in range(N-1, 0, -1):
    if target[n] > target[n-1]:
        for i in range(N-1, n-1, -1):
            if target[i] > target[n-1]:
                target[i], target[n-1] = target[n-1], target[i]
                front = target[:n]
                back = sorted(target[n:])
                result = front + back
                break
        break
        

if result:
    print(*result)
else:
    print(-1)