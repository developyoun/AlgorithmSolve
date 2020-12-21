from collections import deque
dq = deque()
answer = []
for _ in range(int(input())):
    info = input().split()
    text = info[0]

    if text == 'push_front':
        dq.appendleft(info[1])
    elif text == 'push_back':
        dq.append(info[1])
    elif text == 'pop_front':
        if dq: answer.append(dq.popleft())
        else: answer.append(-1)
    elif text == 'pop_back':
        if dq: answer.append(dq.pop())
        else: answer.append(-1)
    elif text == 'size':
        answer.append(len(dq))
    elif text == 'empty':
        if dq: answer.append(0)
        else: dq: answer.append(1)
    elif text == 'front':
        if dq: answer.append(dq[0])
        else: answer.append(-1)
    else:
        if dq: answer.append(dq[-1])
        else: answer.append(-1)
print('\n'.join(map(str, answer)))