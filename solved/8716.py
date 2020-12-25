x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if x2 < x3 or x4 < x1 or y1 < y4 or y3 < y2:
    print(0)
else:
    a, b, c, d = max(x1, x3), max(y2, y4), min(x2, x4), min(y1, y3)
    print((c-a)*(d-b))
