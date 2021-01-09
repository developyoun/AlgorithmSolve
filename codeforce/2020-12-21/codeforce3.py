from collections import deque

for _ in range(int(input())):
    N, M = map(int, input().split())
    queue = deque()
    
    rows = [False] * N
    cols = [False] * N
    for m in range(M):
        r, c = map(int, input().split())
        queue.append([r-1, c-1]) 
        rows[r-1] = True
        cols[c-1] = True
    
    cnt = 0
    tmp = deque()
    while queue:
        y, x = queue.popleft()

        if x == y:
            continue
        if not cols[y]:
            cols[x] = False
            rows[x] = True
            cnt += 1
        elif not rows[x]:
            rows[y] = False
            cols[y] = True
            cnt += 1
        else:
            tmp.append([y, x])

    flag = 0
    while tmp:
        y, x = tmp.popleft()

        if x == y:
            continue
        if not cols[y]:
            cols[x] = False
            rows[x] = True
            cnt += 1
        elif not rows[x]:
            rows[y] = False
            cols[y] = True
            cnt += 1
        else:
            flag += 1
    
    if flag:
        cnt += flag + 1
    print(cnt)