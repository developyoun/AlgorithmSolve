from itertools import combinations

def solve():
    if k-5 < 0:
        return 0

    result = 0
    for tmp in combinations(s, k-5):
        target = set(tmp)
        cnt = 0
        for words in arr:
            if not words - target:
                cnt +=1
        result = max(result, cnt)
    
    return result



N, k = map(int, input().split())
rest = set('antci')

s = set('abcdefghijklmnopqrstuvwxyz')
s -= rest

arr = []
for _ in range(N):
    string = set(input())
    arr.append(string-rest)

print(solve())
