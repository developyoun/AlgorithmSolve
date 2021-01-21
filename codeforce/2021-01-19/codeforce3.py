from collections import defaultdict

def solve(target, depth, tmp):
    global flag,result

    if flag:
        return

    if depth == N:
        result = tmp[:]
        flag = True
        return

    for key, value in dic.items():
        if not value: continue
        other = target - key
        if other == key and value <= 1: continue
        if other in dic and dic[other]:
            dic[key] -= 1; dic[other] -= 1
            solve(max(key, other), depth+1, tmp + [key, other])
            dic[key] += 1; dic[other] += 1

for _ in range(int(input())):
    N = int(input())

    visited = [0] * 2*N
    dic = defaultdict(int)
    arr = sorted(list(map(int, input().split())), reverse=True)
    for a in arr: dic[a] += 1

    x = arr[0]
    dic[x] -= 1

    flag = False
    result = []
    for k in dic.keys():
        if dic[k]:
            dic[k] -= 1
            solve(arr[0], 1, [arr[0], k])
            dic[k] += 1
        
    if flag:
        print('YES')
        print(result[0]+result[1])
        for i in range(0, 2*N, 2):
            print(result[i], result[i+1])
    else:
        print('NO')