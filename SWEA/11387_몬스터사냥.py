for case in range(1, int(input())+1):
    D, L, N = map(int, input().split())

    total = D
    for n in range(1, N):
        total += D+D*n*L*0.01
    print('#{} {}'.format(case, int(total)))
