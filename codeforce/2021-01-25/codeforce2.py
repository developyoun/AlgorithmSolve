for _ in range(int(input())):
    N = int(input())

    rest = N % 10
    N -= rest * 2021
    
    n, flag = 0, False
    while N - 2021*n >= 0:
        now = N - 2021*n
        if not now % 2020:
            flag = True
            break
        n += 10
    
    if flag:
        print('YES')
    else:
        print('NO')