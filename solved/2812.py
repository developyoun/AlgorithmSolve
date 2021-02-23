N, K = map(int, input().split())
number = input()

stack = []
for i in range(N):
    if not stack:
        stack.append(number[i])
    elif stack[-1] < number[i]:
        while K and stack and stack[-1] < number[i]:
            stack.pop()
            K -= 1
        stack.append(number[i])
    else:
        stack.append(number[i])
while K: 
    stack.pop(); K-=1
print(''.join(stack))