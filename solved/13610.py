a, b = map(int, input().split())
c = b - a
print(a//c + (2 if a%c else 1))