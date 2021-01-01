ans = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())

    res = 0
    if a == b == c:
        res = 10000+a*1000
    elif a != b and a != c and b != c:
        res = 100*max(a, b, c)
    else:
        if a == b:
            res = 1000 + 100*a
        else:
            res = 1000 + 100*c
    ans = max(ans, res)
print(ans)