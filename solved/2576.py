arr = [int(input()) for _ in range(7)]
res = list(filter(lambda x: x & 1, arr))
if res:
    print(sum(res))
    print(min(res))
else:
    print(-1)