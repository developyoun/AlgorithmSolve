from itertools import permutations
arr = [input() for _ in range(6)]

result = []
for perm in permutations(arr, 3):
    whole = list(arr)
    for p in perm:
        whole.remove(p)
    
    for x in range(3):
        string = ''
        for y in range(3):
            string += perm[y][x]
        if string in whole:
            whole.remove(string)
    if not whole:
        result = perm
        break

if result:
    for r in result:
        print(r)
else:
    print(0)