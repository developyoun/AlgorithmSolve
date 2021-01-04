for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    one = arr.count(1)
    two = N - one

    answer = 0
    if not one & 1 and (not two & 1 or (two&1 and one >= 2)):
        answer = 1
    print('YES' if answer else 'NO')