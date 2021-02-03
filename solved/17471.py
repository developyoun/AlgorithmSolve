from itertools import combinations

def connect(numbers):
    visited = [False]*N
    visited[numbers[0]] = True
    q = [numbers[0]]

    cnt, value = 1, values[numbers[0]]
    while q:
        now = q.pop()
        for new in info[now]:
            if not visited[new] and new in numbers:
                visited[new] = True
                q.append(new)
                value += values[new]
                cnt += 1

    if cnt != len(numbers): return 0
    else: return value



N = int(input())
values = list(map(int, input().split()))
info = [[] for _ in range(N)]
for n in range(N):
    li = list(map(lambda x:int(x)-1, input().split()))
    info[n].extend(li[1:])

result = 1001
whole = set(i for i in range(N))
for n in range(1, N//2+1):
    for comb in combinations(range(N), n):
        A = set(comb)
        B = whole - A

        resA, resB = connect(list(A)), connect(list(B))
        if resA and resB:
            result = min(result, abs(resA-resB))
print(result if result != 1001 else -1)