MAX = 1000001
flag = [0] * MAX
for i in range(2, MAX):
    if flag[i]: continue
    for j in range(i+i, MAX, i):
        flag[j] = True

for _ in range(int(input())):
    N = int(input())

    result = 0
    a = 1+N
    while flag[a]: a += 1
    b = a+N
    while flag[b]: b += 1
    
    result = a*b
    print(result)