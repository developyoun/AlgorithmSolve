N, X, K = map(int, input().split())

info = [0] * N
info[X-1] = 1
for _ in range(K):
    a, b = map(int, input().split())
    info[a-1], info[b-1] = info[b-1], info[a-1]
print(info.index(1)+1)