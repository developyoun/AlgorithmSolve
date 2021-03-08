N, M = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]
li = [int(input()) for _ in range(M)]

start = 1
cnt = 1
for m in range(M):
    start += li[m]
    if start >= N:
        break
    start += arr[start]
    if start >= N:
        break
    cnt += 1
print(cnt)