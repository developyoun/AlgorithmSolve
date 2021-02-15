def gcd(x, y):
    while y:
        x, y = y, x%y
    return x == a

a, b = map(int, input().split())

res1, res2 = 0, 0
c = a*b
for i in range(a, b+1, a):
    j = c //i
    if j < i: 
        break
    if not c % i and gcd(i, j):
        res1, res2 = i, j
print(res1, res2)