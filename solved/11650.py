import heapq
arr = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    heapq.heappush(arr, [x, y])
while arr:
    print(*heapq.heappop(arr))