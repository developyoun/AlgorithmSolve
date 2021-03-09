from collections import deque

def solution(priorities, location):
    answer = 0

    dq = deque()
    l = len(priorities)
    for i in range(l):
        dq.append([priorities[i], i])

    idx = 0
    priority = sorted(priorities, reverse=True)
    while dq:
        if dq[0][0] == priority[idx]:
            idx += 1
            if dq[0][1] == location:
                break
            else:
                dq.popleft()
                answer += 1
        else:
            dq.append(dq.popleft())
        
    return answer

solution([2, 1, 3, 2], 2)