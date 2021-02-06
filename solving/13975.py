from heapq import heappush, heappop

for _ in range(int(input())):
    N = int(input())
    heap = []
    for size in map(int, input().split()):
        heappush(heap, size)

    total = 0
    while len(heap) > 1:
        a, b = heappop(heap), heappop(heap)
        heappush(heap, a+b)
        total += a+b
    print(total)