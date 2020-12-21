from collections import deque
A, B = map(int, input().split())
answer = -1

dq = deque([[A, 1]])
while dq:
    num, cnt = dq.popleft()

    if num == B:
        answer = cnt; break

    num1, num2 = num*2, num*10+1
    if num1 <= B: dq.append([num1, cnt+1])
    if num2 <= B: dq.append([num2, cnt+1])

print(answer)