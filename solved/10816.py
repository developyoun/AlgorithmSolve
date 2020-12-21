from collections import defaultdict
N = int(input())
get = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

dic = defaultdict(int)
for g in get:
    dic[g] += 1

print(' '.join(map(str, [dic[n] for n in numbers])))
