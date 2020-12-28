while True:
    num = input()
    if num == '0': break

    l = len(num)
    one = num.count('1')
    zero = num.count('0')

    result = (l+1) + one*2 + zero*4 + (l-one-zero)*3
    print(result)