N = int(input())
a = 5
b = 12

if N == 1:
    print(a)
elif N >= 2:
    for _ in range(3, N+1):
        b, a = b+(b-a+3), b
        b %= 45678
        a %= 45678
    print(b)