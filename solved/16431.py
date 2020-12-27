r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
r3, c3 = map(int, input().split())

b = abs(r3-r1) + abs(c3-c1) - min(abs(r3-r1), abs(c3-c1))
d = abs(r2-r3) + abs(c3-c2)
if b == d:
    print('tie')
elif b < d:
    print('bessie')
else:
    print('daisy')