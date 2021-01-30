for case in range(1, int(input())+1):
    N = int(input())
    
    flag = True
    upper = 1
    while N > 0:
        N -= upper
        if flag: upper *= 4
        flag = not flag

    print('#{} {}'.format(case, 'Alice' if flag else 'Bob'))