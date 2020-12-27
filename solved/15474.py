a, b, c, d, e = map(int, input().split())

f = a//b + (1 if a % b else 0)
g = a//d + (1 if a % d else 0)

print(min(f*c, e*g))