while True:
    try:
        X = int(input()) * 10**7
        N = int(input())
        arr = [int(input()) for _ in range(N)]
        arr.sort()

        res1, res2 = -1, -1
        left, right = 0, N-1
        while left < right:
            Sum = arr[left] + arr[right]
            if Sum == X:
                if arr[right]-arr[left] >= res2 - res1:
                    res1, res2 = arr[left], arr[right]
                left, right = left+1, right-1
            elif Sum > X:
                right -= 1
            else:
                left += 1

        if [res1, res2] == [-1, -1]:
            print('danger')
        else:
            print('yes', res1, res2)
    except:
        break