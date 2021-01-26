for _ in range(int(input())):
    N = int(input())

    while not N % 2 and N > 1:
        N //= 2
        
    print('NO' if N == 1 else 'YES')