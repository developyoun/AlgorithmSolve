import sys
input = sys.stdin.readline

stack = []
result = ''
for s in input().rstrip():
    if 'A' <= s <= 'Z':
        result += s
    elif s in '()':
        if s == '(': stack.append(s)
        else:
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
    else:
        if s in '+-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(s)
        else:
            while stack and stack[-1] in '*/' and stack[-1] != '(':
                result += stack.pop()
            stack.append(s)

while stack: result += stack.pop()
print(result)