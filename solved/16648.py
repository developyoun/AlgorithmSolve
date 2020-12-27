t, p = map(int, input().split())

if p <= 20:
    c = 80/t + (40-2*p)/t
    print(2*p/c)
else:
    c = (100-p)/t
    print((p-20)/c + 40/c)