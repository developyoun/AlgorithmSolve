for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    cost = [0] + list(map(int, input().split()))

    flag = [False] * m
    people = sorted(arr, reverse=True)
    
    result = 0
    idx = 1
    for p in people:
        if idx < m and not flag[idx]:
            pay, present = cost[p], cost[idx]
            if present < pay:
                result += present
                idx += 1
            else:
                result += pay
        else:
            result += cost[p]
    print(result)