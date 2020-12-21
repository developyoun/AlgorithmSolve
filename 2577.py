numbers = [int(input()) for _ in range(3)]
total = 1
for num in numbers: total *= num

print(total)
for i in range(10):
    print(str(total).count(str(i)))