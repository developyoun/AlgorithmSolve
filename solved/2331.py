num, p = input().split()
p = int(p)
arr = [num]

idx = -1
while True:

    new = 0
    for n in num:
        new += int(n)**p
    num = str(new)

    if num in arr:
        idx = arr.index(num)
        break
    arr.append(num)
print(idx)