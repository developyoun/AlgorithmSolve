N = int(input())
numbers = set(input().split())
M = int(input())
checked = list(input().split())

result = set(checked) - numbers
answer = []
for m in checked:
    if m in result: answer.append('0')
    else: answer.append('1')
print('\n'.join(answer))