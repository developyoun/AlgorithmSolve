N = int(input())
arr = list(map(int, input().split()))

result1, result2 = 0, 0
for a in arr:
    result1 += 10 + (a//30)*10
    result2 += 15 + (a//60)*15

if result1 == result2:
    print('Y', 'M', result1)
elif result1 > result2:
    print('M', result2)
else:
    print('Y', result1)