N, M = map(int, input().split())
total, result = 0, -1

for n in range(N):
    ml, per = map(int, input().split())
    total += ml * per
    if result == -1 and total > M * 100: 
        result = n+1

print(result)