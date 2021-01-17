N = int(input())

l = len(str(N))
calc = (N - 10**(l-1) + 1)
cnt = calc * l
N -= calc

while N:
    a = len(str(N))
    val = N+1 - 10**(a-1)
    cnt += val * a
    N -= val

print(cnt)