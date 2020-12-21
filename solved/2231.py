target = int(input())

answer = float('INF')

for i in range(1, 10**6+1):
    num = i
    for s in str(i):
        num += int(s)
    if num == target: 
        answer = i
        break
print(0 if answer == float('INF') else answer)