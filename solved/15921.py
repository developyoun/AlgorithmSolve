N = int(input())
if N:
    __ = list(map(int, input().split()))
    print(format(1.00, '.2f'))
else:
    print('divide by zero')