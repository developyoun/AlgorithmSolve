while True:
    arr = list(map(int, input().split()))
    s = sum(arr)
    if not s : break

    if s/6 != 6:
        s -= (max(arr)+min(arr))
        print(s/4)
    else:
        print(6)