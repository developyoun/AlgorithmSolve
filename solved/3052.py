numbers = [int(input()) for _ in range(10)]

s = set()
for num in numbers:
    val = num % 42
    s.add(val)
print(len(s))