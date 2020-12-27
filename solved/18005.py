n = int(input())

if n & 1:
    print(0)
else:
    if n//2 & 1:
        print(1)
    else:
        print(2)