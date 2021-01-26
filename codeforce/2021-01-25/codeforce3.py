for _ in range(int(input())):
    Na, Nb, N = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    boy = [[] for _ in range(Na+1)]
    girl = [[] for _ in range(Nb+1)]

    for i in range(N):
        a, b = A[i], B[i]
        boy[a].append(b)
        girl[b].append(a)

    total = N*(N-1) // 2

    for idx in range(1, Na+1):
        numB = len(boy[idx])
        if numB > 1:
            total -= numB - 1
    for idx in range(1, Nb+1):
        numG = len(girl[idx])
        if numG > 1:
            total -= numG - 1
            
    print(total)