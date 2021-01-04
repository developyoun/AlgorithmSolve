for _ in range(int(input())):
    N = int(input())
    save = []
    for n in range(N):
        a, b = map(int, input().split())
        a, b = max(a, b), min(a, b)
        save.append([a, b, n+1])
    
    arr = sorted(save, key=lambda x: (x[0], x[1]))
    answer = []
    for h, w, m in save:
        if m == arr[0][2]:
            if N > 1:
                x, y, n = arr[1]
            else:
                x, y, n = h+1, w+1, -1
        else: 
            x, y, n = arr[0]

        if h > x and w > y:
            answer.append(n)
        else:
            answer.append(-1)
    print(*answer)

    