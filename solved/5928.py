a, b, c = map(int, input().split())
a, b, c = a-11, b-11, c-11
a *= 1440
b *= 60
total = a + b + c
print(total if total >= 0 else -1)