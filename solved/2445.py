N = int(input())

arr = [' ']*(2*N)
for n in range(2*N-1):
    if n < N:
        arr[n] = '*'
        arr[-n-1] = '*'
    else:
        arr[n] = ' '
        arr[-n-1] = ' '
    print(''.join(arr))
