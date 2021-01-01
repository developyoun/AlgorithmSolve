N = int(input())

for n in range(N):
    print(' '*n+'*'*(2*(N-n)-1))

for n in range(N-1, 0, -1):
    print(' '*(n-1) + '*'*(2*(N-n)+1))