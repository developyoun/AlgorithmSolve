N = int(input())
arr = sorted([int(input()) for _ in range(N)], reverse=True)

res = 0
total = 0
for i in range(N):
    total += arr[i]
    val = total//(i+1)
    res = max(res, val, arr[i]*(i+1))
print(res)