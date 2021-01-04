from heapq import heappush, heappop

for _ in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = []
    for a in arr:
        heappush(heap, -a)
    
    a, b = 0, 0
    for i in range(N):
        num = -heappop(heap)

        if not i & 1:
            if num & 1:
                continue
            else:
                a += num
        else:
            if num & 1:
                b += num
            else:
                continue
    if a > b:
        print('Alice')
    elif b > a:
        print('Bob')
    else:
        print('Tie')
