def solve(n, total, arr):
    global answer

    if total >= N:
        if total == N:
            val = int(''.join(map(str, arr)))
            answer = min(answer, val)
        return
    
    for k in range(n+1, 10):
        solve(k, total + k, arr + [k])


for _ in range(int(input())):
    N = int(input())

    answer = float('INF')
    if N < 10:
        answer = N
    else:
        for i in range(1, 10):
            solve(i, i, [i])
    
    print(-1 if answer == float('INF') else answer)