a, b, c = map(int, input().split())

t = min(a//2, b)

while t > 0 and (a-2*t + b-t) < c:
    t -= 1

print(t)