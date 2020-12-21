import heapq

arr = []
answer = []
for _ in range(int(input())):
    val = int(input())

    if val:
        heapq.heappush(arr, -val)
    else:
        if arr:
            answer.append(-heapq.heappop(arr))
        else:
            answer.append(0)
print('\n'.join(map(str, answer)))