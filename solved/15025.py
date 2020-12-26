a, b = map(int, input().split())

if [a, b] == [0, 0]:
    print('Not a moose')
elif a == b:
    print('Even {}'.format(a+b))
else:
    print('Odd {}'.format(max(a, b)*2))