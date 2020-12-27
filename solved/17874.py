a, b, c = map(int, input().split())

p, q = max(a-b, b), max(a-c, c)
print(p*q*4)