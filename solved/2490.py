for _ in range(3):
    arr = list(map(int, input().split()))
    cnt = arr.count(0)

    if not cnt:
        print('E')
    elif cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')