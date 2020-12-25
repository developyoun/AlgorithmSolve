a, b, c = map(int, input().split())
b -= a
print(b//c + (1 if b%c else 0))