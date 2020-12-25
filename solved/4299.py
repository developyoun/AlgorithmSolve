n1, n2 = map(int, input().split())
a = (n1 + n2)/2
b = n1-a

if int(a) == a and int(b) == b and a >= 0 and b >=0:
    a, b = int(a), int(b)
    print(max(a, b), min(a, b))
else:
    print(-1)