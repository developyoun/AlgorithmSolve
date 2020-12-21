start, end = map(int, input().split())
check_arr = [False] * (end-start+1)

result = 0

n = 2
while n**2 <= end:
    double = n**2

    if start % double:
        std = (start // double +1) * double
    else:
        std = start

    while std <= end:
        check_arr[end-std] = True
        std += double
    n += 1

print(check_arr.count(False))