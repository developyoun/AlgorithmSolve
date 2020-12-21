for _ in range(int(input())):
    k = int(input())
    n = int(input())

    arr = [[0]*15 for _ in range(15)]
    for i in range(15):
        arr[0][i] = i
    
    for f in range(1, k+1):
        tmp = arr[f-1]
        for h in range(1, n+1):
            arr[f][h] = sum(tmp[:h+1])
    print(arr[k][n])