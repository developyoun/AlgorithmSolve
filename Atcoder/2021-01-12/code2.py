N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(i+1, N):
        if arr[i][0] - arr[j][0]:
            value = (arr[i][1] - arr[j][1]) / (arr[i][0] - arr[j][0])
            if -1 <= value <= 1:
                result += 1
print(result)