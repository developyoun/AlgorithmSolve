a, b = input().split()
A = sum(list(map(int, a)))
B = sum(list(map(int, b)))
result = max(A, B)
print(result)