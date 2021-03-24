N, K = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)], reverse=True)
print(sum(arr[:K]))
