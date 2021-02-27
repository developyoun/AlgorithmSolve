result = float('INF')
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    if A < C:
        result = min(result, B)

print(-1 if result == float('INF') else result)