a, b = map(int, input().split())

res = [a, b]
for _ in range(int(input())):
    x, y = map(int, input().split())

    if res[0]/res[1] > x/y:
        res = [x, y]

print(format(1000/res[1]*res[0], '.2f'))    