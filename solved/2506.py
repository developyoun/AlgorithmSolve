N = int(input())
arr = list(map(int, input().split()))

cnt = 0
result = 0
for a in arr:
    if a:
        cnt += 1
        result += cnt
    else:
        cnt = 0
print(result)