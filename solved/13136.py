a, b, c = map(int, input().split())
x1 = a//c + (1 if a%c else 0)
x2 = b//c + (1 if b%c else 0)
print(x1 * x2)