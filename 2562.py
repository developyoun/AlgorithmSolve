numbers = [int(input()) for _ in range(9)]
MAX = max(numbers)
print(MAX)
print(numbers.index(MAX)+1)