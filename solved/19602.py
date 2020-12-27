t = 0
for i in range(1, 4):
    t += int(input()) * i

print('happy' if t >= 10 else 'sad')