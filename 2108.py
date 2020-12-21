N = int(input())
numbers = []
arr = [0]*8001
for _ in range(N):
    n = int(input())
    numbers.append(n)
    arr[n] += 1

max_cnt = max(arr)
if arr.count(max_cnt) >= 2:
    cnt = 2
else:
    cnt = 1

index = -4000
while index < 4000:
    if arr[index] == max_cnt:
        cnt -= 1
    if not cnt: break
    index += 1

numbers.sort()

print(round(sum(numbers)/N))
print(numbers[N//2])
print(index)
print(numbers[-1] - numbers[0])