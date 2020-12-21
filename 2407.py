N, R = map(int, input().split())
table = [[0]*(R+1) for _ in range(N+1)]

for i in range(N+1):
    table[i][0] = 1
for j in range(1, R+1):
    table[j][1] = j

for n in range(1, N+1):
    for r in range(1, R+1):
        table[n][r] = table[n-1][r] + table[n-1][r-1]

print(table[N][R])