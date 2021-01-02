N = int(input())
a, b = 1, 0
for _ in range(1, N):
    a, b = a+b, a

print(a)