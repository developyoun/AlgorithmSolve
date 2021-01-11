N, C = map(int, input().split())

result = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    result += (b-a+1) * min(C, c)
print(result)