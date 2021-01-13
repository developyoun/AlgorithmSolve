from itertools import combinations

arr = [int(input()) for _ in range(9)]

for liter in combinations(arr, 7):
    value = sum(liter)
    if value == 100:
        print('\n'.join(map(str, sorted(liter))))
        break