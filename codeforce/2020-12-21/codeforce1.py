for _ in range(int(input())):
    N = int(input())
    string = input()
    cnt = 0
    idx = N-1
    while 0 <= idx and string[idx] == ')':
        cnt += 1
        idx -= 1
    print('YES' if cnt > N//2 else 'NO')