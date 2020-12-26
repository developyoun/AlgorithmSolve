a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

res = 0
if a1 < a2:
    res += a2-a1
if b1 < b2:
    res += b2-b1
if c1 < c2:
    res += c2-c1
print(res)