N = int(input())

for n in range(N):
    print(' '*(N-n-1) + '*'*(n+1))
for n in range(1, N):
    print(' '*(N-n-1) + '*'*(n+1))