N = int(input())
numbers = [int(input()) for _ in range(N)]

stack = []
answer = []
def solve():
    idx = 0

    for i in range(1, N+1):
        stack.append(i)
        answer.append('+')
        while stack and stack[-1] == numbers[idx]:
            stack.pop()
            answer.append('-')
            idx += 1
    return 'NO' if stack else '\n'.join(answer)

print(solve())