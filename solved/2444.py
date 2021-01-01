N = int(input())

for n in range(N):
    print(' '*(N-n-1) + '*'*(2*n+1))

for n in range(N-1, 0, -1):
    print(' '*(N-n) + '*'*(2*n-1))