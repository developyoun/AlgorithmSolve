a, b, c = map(int, input().split())

for i in range(c+1):
    if a*i + b*(i//7) >= c:
        print(i)
        break