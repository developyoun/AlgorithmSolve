a, b = map(int, input().split())
c = int(input())
h, m = c//60, c%60
a, b = a+h, b+m

if b >= 60:
    a += 1
    b -= 60
if a >= 24:
    a -= 24
print(a, b)