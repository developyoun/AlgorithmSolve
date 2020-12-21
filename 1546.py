N = int(input())
numbers = list(map(int, input().split()))
total = 0
MAX= max(numbers)

for num in numbers:
    total += num/MAX * 100

print(total/N)