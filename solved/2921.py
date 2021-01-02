N = int(input())
# 1 + 2 = 3
# 2 + 3 + 4 = 9
# 3 + 4 + 5 + 6 = 18
# 4 + 5 + 6 + 7 + 8 = 30
c = 3
for n in range(2, N+1):
    total = c
    for m in range(n, n*2+1):
        total += m
    c = total
print(c)