N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

K = int(input())
target = set(map(int, input().split()))

visited = [[0]*(N+1) for _ in range(K+1)]
