a, b = map(int, input().split())

res = 0
if a*3 <= b:
    res = max(res, a)
if b*3 <= a:
    res = max(res, b)
if (a/2)*2 <= b:
    res = max(res, a/2)
if (b/2)*2 <= a:
    res = max(res, b/2)
if (a/3) <= b:
    res = max(res, a/3)
if (b/3) <= a:
    res = max(res, b/3)
print(res)