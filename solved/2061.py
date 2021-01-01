K, L = map(int, input().split())

flag = True
for i in range(2, L):
    if not K % i:
        flag = False
        break
if flag:
    print('GOOD')
else:
    print('BAD', i)