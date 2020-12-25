x, k = map(int, input().split())
x, k = x*1000, k*1000

if 7*k <= x:
    print(7*k)
elif 7*k <= 2*x:
    print(7*k//2)
elif 7*k <= 4*x:
    print(7*k//4)
else:
    print(0)