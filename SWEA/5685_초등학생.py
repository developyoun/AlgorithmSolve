for case in range(1, int(input())+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    arr = [[0]*21 for _ in range(N-1)]
    arr[0][numbers[0]] = 1

    for n in range(1, N-1):
        for m in range(21):
            if arr[n-1][m]:
                if 0 <= m + numbers[n] <= 20:
                    arr[n][m+numbers[n]] = (arr[n][m+numbers[n]] + arr[n-1][m]) % 1234567891
                if 0 <= m - numbers[n] <= 20:
                    arr[n][m-numbers[n]] = (arr[n][m-numbers[n]] + arr[n-1][m]) % 1234567891
    print('#{} {}'.format(case, arr[-1][numbers[-1]]))