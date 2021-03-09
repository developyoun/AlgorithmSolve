from math import ceil

def solution(progresses, speeds):
    answer = []

    l = len(progresses)
    stack = []
    for i in range(l):
        val = ceil((100-progresses[i]) / speeds[i])
        if not stack or stack[-1] < val:
            stack.append(val)
            answer.append(1)
        else:
            answer[-1] += 1
        
    return answer