from heapq import heappush, heappop

def solution(jobs):
    answer = 0

    idx, last, now = 0, -1, 0
    arr = []
    while idx < len(jobs):
        for start, work in jobs:
            if last < start <= now:
                heappush(arr, [work, start])
        
        if arr:
            w, s = heappop(arr)
            last = now
            now += w
            answer += now - s
            idx += 1
        else:
            now += 1
    
    return answer // len(jobs)