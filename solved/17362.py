n = int(input())

n = (n-1)%8
n += 1
if n in (1, 9):
    print(1)
elif n in (2, 8):
    print(2)
elif n in (3, 7):
    print(3)
elif n in (4, 6):
    print(4)
else:
    print(5)