N = int(input())

num = 1
upper = 1
cnt = 2
while num < N:
    if num & 1:
        upper += 1
    cnt += upper
    num += 1
    
print(cnt)