arr = list(map(int, input().split()))

if sum(arr) >= 100:
    print('OK')
else:
    i = arr.index(min(arr))
    if i == 0:
        print('Soongsil')
    elif i == 1:
        print('Korea')
    else:
        print('Hanyang')