from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dic = defaultdict(int)
for _ in range(N):
    s = input().rstrip()
    if len(s) < M: continue
    dic[s] += 1

arr = [[] for _ in range(N+1)]
for k, v in dic.items():
    arr[v].append(k)

result = []
for i in range(N, 0, -1):
    if not arr[i]: continue
    if len(arr[i]) == 1:
        result.append(arr[i][0])
    else:
        newArr = sorted(arr[i], key=lambda x: (-len(x), x))
        for s in newArr:
            result.append(s)
print('\n'.join(result))