from collections import deque
N = int(input())

dq = deque()
answer = []
for _ in range(N):
    info = input().split()

    if info[0] == 'push':
        dq.append(info[1])
    elif info[0] == 'pop':
        if dq: answer.append(dq.popleft())
        else: answer.append(-1)
    elif info[0] == 'size':
        answer.append(len(dq))
    elif info[0] == 'empty':
        if dq: answer.append(0)
        else: answer.append(1)
    elif info[0] == 'front':
        if dq: answer.append(dq[0])
        else: answer.append(-1)
    else:
        if dq: answer.append(dq[-1])
        else: answer.append(-1)

print('\n'.join(map(str, answer)))