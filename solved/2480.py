a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a != b and b != c and a != c:
    print(max(a, b ,c) * 100)
else:
    x = -1
    if c != b:
        x = a
    else:
        x = b
    print(1000 + x * 100)
