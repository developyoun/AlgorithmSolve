N = int(input())

for i in range(N):
    val = ' '*(N-i-1) + '*' * (i+1)
    print(val)