import sys
input = sys.stdin.readline

result = []
for _ in range(3):
    N = int(input())
    value = sum([int(input()) for _ in range(N)])
    result.append('+' if value > 0 else '-' if value else '0')
print('\n'.join(result))