N = int(input())
a, b = 1, 1
for n in range(1, 4):
    a *= N - n
    b *= n
print(a // b)