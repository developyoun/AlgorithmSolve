from heapq import heappop, heappush

def solution(scoville, K):
    answer = 0
    arr = []
    for s in scoville:
        heappush(arr, s)

    cnt = 0
    while len(arr) >= 2 and arr[0] < K:
        val1, val2 = heappop(arr), heappop(arr)
        heappush(arr, val1+val2*2)
        answer += 1
    return answer if arr[0] >= K else -1