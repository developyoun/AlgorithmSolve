N, K = map(int, input().split())
angles = list(map(int, input().split()))
check = list(map(int, input().split()))
visited = [False] * 361

q = [0]
while q:
    now = q.pop()

    for a in angles:
        plus, minus = (now+a)%360, (now-a)%360
        if not visited[plus]:
            visited[plus] = True
            q.append(plus)
        if not visited[minus]:
            visited[minus] = True
            q.append(minus)
            
for c in check:
    if visited[c]:
        print('YES')
    else:
        print('NO')