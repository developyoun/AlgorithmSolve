a = int(input())
b = int(input())

if 0 < a and 0 < b:
    print(1)
elif 0 < a:
    print(4)
elif 0 > a and 0 < b:
    print(2)
else:
    print(3)