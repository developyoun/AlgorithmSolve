from collections import deque

for _ in range(int(input())):
    N, target = map(int, input().split())
    tmp = deque(map(int, input().split()))

    numbers = deque([[i, j] for i, j in zip(tmp, range(N))])
    cnt = 1
    while True:
        if max(tmp) == numbers[0][0]:
            if target == numbers[0][1]: break
            numbers.popleft()
            tmp.popleft()
            cnt += 1
        else:
            numbers.append(numbers.popleft())
            tmp.append(tmp.popleft())
    print(cnt)