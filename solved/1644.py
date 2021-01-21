N = int(input())
flag = [0] * (N+1)
arr = [0, 2]

for n in range(3, N+1, 2):    
    if flag[n]: continue
    arr.append(arr[-1]+n)
    
    for m in range(n, N+1, n):
        flag[m] = True

i, j = 0, 1
result = 0
while j < len(arr):
    val = arr[j] - arr[i]
    if val <= N:
        if val == N:
            result += 1
        j += 1
    else:
        i += 1

print(result)