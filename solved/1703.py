while True:
    arr = list(map(int, input().split()))
    if not arr[0]: break

    total = 1
    for i in range(1, len(arr), 2):
        a, b = arr[i], arr[i+1]
        total *= a
        total -= b
        
    print(total)