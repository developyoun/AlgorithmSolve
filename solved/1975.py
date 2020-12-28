arr = [0] * 1001
for num in range(1, 1001):

    for k in range(2, num+1):
        target = num
        while not target % k:
            arr[num] += 1
            target //= k

result = []
for _ in range(int(input())):
    result.append(str(arr[int(input())]))
print('\n'.join(result))