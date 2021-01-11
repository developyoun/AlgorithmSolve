N = int(input())
arr = list(map(int, input().split()))
num = 2**N

A = max(arr[:num//2])
B = max(arr[num//2:])
a = arr.index(A)
b = arr.index(B)

print(a+1 if A < B else b+1)