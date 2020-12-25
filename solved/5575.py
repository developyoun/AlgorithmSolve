arr = [list(map(int, input().split())) for _ in range(3)]

for a1, b1, c1, a2, b2, c2 in arr:
    a = a2 - a1
    b = b2 - b1
    c = c2 - c1
    if c < 0:
        c += 60
        b -= 1
    if b < 0:
        b += 60
        a -= 1
    print(a, b, c)