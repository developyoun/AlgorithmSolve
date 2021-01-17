from collections import defaultdict

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

a, b = defaultdict(int), defaultdict(int)
for i in range(N):
    total = 0
    for j in range(i, N):
        total += A[j]
        a[total] += 1

for i in range(M):
    total = 0
    for j in range(i, M):
        total += B[j]
        b[total] += 1

result = 0
for key, value in a.items():
    result += value * b[T-key]
print(result)