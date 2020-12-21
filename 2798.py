from itertools import combinations
N, target = map(int, input().split())
numbers = list(map(int, input().split()))

answer = -1
for comb in combinations(set(numbers), 3):
    total = sum(comb)
    if answer < total <= target:
        answer = total
print(answer)