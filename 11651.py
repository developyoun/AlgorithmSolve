arr = []
for _ in range(int(input())):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[1], x[0]))
for x, y in arr:
    print(x, y)