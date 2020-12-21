N = int(input())
numbers = list(map(int, input().split()))

if N == 1:
    print('A')
elif N == 2:
    if numbers[0] == numbers[1]:
        print(numbers[-1])
    else:
        print('A')
else:
    n0, n1, n2 = numbers[0], numbers[1], numbers[2]

    if n1-n0:
        a = (n2-n1)//(n1-n0)
        b = n1 - n0*a
    else:
        a = 0
        b = n1
    
    flag = True
    for i in range(1, N):
        if numbers[i] != a*numbers[i-1] + b:
            flag = False
            break
    
    if flag:
        print(a*numbers[-1] + b)
    else:
        print('B')