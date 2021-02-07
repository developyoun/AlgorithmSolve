from heapq import heappush, heappop

def calc():
    arr = []
    res = 0
    while len(heap) > 1:
        a, b = heappop(heap), heappop(heap)
        heappush(arr, a+b)
        res += a+b
    if heap: arr.append(heappop(heap))
    return arr, res

for _ in range(int(input())):
    N = int(input())
    heap = []
    for size in map(int, input().split()):
        heappush(heap, size)

    total = 0
    while len(heap) > 1:
        heap, tmp = calc()
        total += tmp
        print(heap, total)