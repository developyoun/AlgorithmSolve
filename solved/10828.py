N = int(input())

stack = []
answer = []
for _ in range(N):
    info = input().split()

    if info[0] == 'push':
        stack.append(info[1])
    elif info[0] == 'top':
        if stack: answer.append(stack[-1])
        else: answer.append(-1)
    elif info[0] == 'size':
        answer.append(len(stack))
    elif info[0] == 'empty':
        if stack: answer.append(0)
        else: answer.append(1)
    elif info[0] == 'pop':
        if stack: answer.append(stack.pop())
        else: answer.append(-1)

print('\n'.join(map(str, answer)))