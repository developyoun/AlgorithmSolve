N, S = map(int, input().split())
numbers = list(map(int, input().split()))
li = [0]
for n in numbers:
    li.append(li[-1]+n)

i, j = 0, 1
MAX = float('INF')
result = MAX
while j <= N:

    if li[j] - li[i] < S:
        j += 1
    else:
        result = min(result, j - i)
        i += 1
        
print(0 if result == MAX else result)