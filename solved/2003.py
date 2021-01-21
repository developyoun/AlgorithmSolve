N, S = map(int, input().split())
numbers = list(map(int, input().split()))
li = [0]
for n in numbers:
    li.append(li[-1]+n)

i, j = 0, 1
result = 0
while j <= N:

    if li[j] - li[i] <= S:
        if li[j] - li[i] == S:
            result += 1
        j += 1
    else:
        i += 1
        
print(result)