arr = [[] for _ in range(201)]

for _ in range(int(input())):
    old, name = input().split()
    arr[int(old)].append(name)

for i in range(1, 201):
    if arr:
        for a in arr[i]:
            print(i, a)