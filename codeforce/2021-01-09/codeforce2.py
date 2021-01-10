from collections import deque

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    queue = deque()
    for a in arr:
        queue.append([a, 1])
    total = 0

    while queue:
        now, cnt = queue.popleft()
        total += now * cnt
        if now % x: break

        queue.append([now//x, cnt*x])

    while queue:
        val, num = queue.popleft()
        total += val * num
        
    print(total)