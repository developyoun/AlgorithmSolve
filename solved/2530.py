a, b, c = map(int, input().split())
d = int(input())
m, s = d//60, d%60
h, m = m//60, m%60
a, b, c = a+h, b+m, c+s
if c >= 60:
    c -= 60
    b += 1
if b >= 60:
    b -= 60
    a += 1
if a >= 24:
    a %= 24
print(a, b, c)