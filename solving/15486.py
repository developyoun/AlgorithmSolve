N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

table = [0]*(N+1)
for i in range(N):
    day, price = arr[i]
    if i + day <= N:
        table[i+day] = max(table[i+day], table[i]+price)
    table[i+1] = max(table[i+1], table[i])
print(table[-1])