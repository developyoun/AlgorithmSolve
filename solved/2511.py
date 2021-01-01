arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

flag = 0
A, B = 0, 0
for i in range(10):
    a, b = arr1[i], arr2[i]
    if a > b:
        flag = 1
        A += 3
    elif a < b:
        flag = 2
        B += 3
    else:
        A += 1
        B += 1

print(A, B)
if A > B:
    print('A')
elif A < B:
    print('B')
else:
    if not flag:
        print('D')
    elif flag == 1:
        print('A')
    else:
        print('B')