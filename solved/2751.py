N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
print('\n'.join(map(str, numbers)))