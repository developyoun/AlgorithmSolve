from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1: break

    for comb in combinations(arr[1:], 6):
        print(*comb)
    print()