import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    arr = [0] + list(map(int, input().split()))

    result = N

    visited = [False] * (N+1)
    visited[0] = True
    for i in range(1, N+1):
        if visited[i]: continue
        visited[i] = True
        save = [i]

        idx = arr[i]
        while not visited[idx]:
            visited[idx] = True
            save.append(idx)
            idx = arr[idx]
        if idx in save:
            start = save.index(idx)
            result -= len(save[start:])
    print(result)