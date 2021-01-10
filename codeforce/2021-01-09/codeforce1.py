for _ in range(int(input())):
    N = int(input())
    
    if N == 1:
        result = '9'
    else:
        result = '98'
        s = '9012345678'
        idx = 0
        while len(result) < N:
            result += s
    
    print(result[:N])

    