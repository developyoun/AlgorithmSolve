import heapq, sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())

    check_arr = [False] * K
    min_heap, max_heap = [], []
    for idx in range(K):
        alpha, value = input().split()
        value = int(value)

        if alpha == 'I':
            heapq.heappush(min_heap, [value, idx])
            heapq.heappush(max_heap, [-value, idx])
            check_arr[idx] = True

        elif value == -1:
            while min_heap and not check_arr[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                __, target_idx = heapq.heappop(min_heap)
                check_arr[target_idx] = False

        elif value == 1:
            while max_heap and not check_arr[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                __, target_idx = heapq.heappop(max_heap)
                check_arr[target_idx] = False

    while max_heap and not check_arr[max_heap[0][1]]: heapq.heappop(max_heap)
    while min_heap and not check_arr[min_heap[0][1]]: heapq.heappop(min_heap)
    
    if not (max_heap or min_heap):
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])