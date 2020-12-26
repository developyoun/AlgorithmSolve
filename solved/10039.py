arr = [int(input()) for _ in range(5)]
t = 0
for a in arr:
    if a < 40:
        a = 40
    t += a
print(t//5)