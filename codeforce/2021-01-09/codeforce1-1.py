from math import ceil

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    total = 0
    MIN, MAX = 0, 0
    for a in arr:
        MIN += a
        MAX += ceil(a/x)
    print(ceil(MIN/x), MAX)