res, ans = 0, 0
for _ in range(10):
    a, b = map(int, input().split())
    res += b-a
    ans = max(res, ans)
print(ans)