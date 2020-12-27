x, l, r = map(int, input().split())

if l <= x <= r:
    print(x)
elif abs(r-x) > abs(l-x):
    print(l)
else:
    print(r)