N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: (2*x[0]+x[1]))

totalB, totalA = 0, 0
for a, b in arr:
    totalA += a

result = 0
while arr and totalB <= totalA:
    a, b = arr.pop()
    totalB += a + b
    totalA -= a
    result += 1
    
print(result)