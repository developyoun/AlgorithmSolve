for _ in range(int(input())):
    w, h, n = map(int, input().split())
    t = 1
    
    while w and not w % 2:
        w //= 2
        t *= 2
    while h and not h % 2:
        h //= 2
        t *= 2
    if t >= n:
        print('YES')
    else:
        print('NO')