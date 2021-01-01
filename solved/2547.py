for _ in range(int(input())):
    __ = input()
    N = int(input())

    arr = [int(input()) for _ in range(N)]
    
    if not sum(arr) % N:
        print('YES')
    else:
        print('NO')