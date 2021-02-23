for _ in range(int(input())):
    N = int(input())
    li = [0] + list(map(int, input().split()))

    cnt = 0
    visited = [False] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            cnt += 1
            visited[i], idx = True, li[i]
            while not visited[idx]:
                visited[idx] = True
                idx = li[idx]
    print(cnt)