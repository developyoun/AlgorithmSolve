from itertools import combinations
import sys
input = sys.stdin.readline

N, l = map(int, input().split())
arr = sorted(input().split())
target = set('aueoi')

answer = []
for comb in combinations(arr, N):
    set_comb = set(comb)
    if set_comb & target and len(set_comb - target) >= 2:
        answer.append(''.join(comb))

print('\n'.join(answer))