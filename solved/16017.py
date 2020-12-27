num = [input() for _ in range(4)]

if num[0] in ('8', '9') and num[1] == num[2] and num[3] in ('8', '9'):
    print('ignore')
else:
    print('answer')