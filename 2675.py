for _ in range(int(input())):
    N, string = input().split()
    N = int(N)
    for s in string:
        print(s*N, end='')
    print()