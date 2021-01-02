cnt = 1
while True:
    a, b, c = map(float, input().split())
    if not b: break

    distance = a*3.1415927*b/(12*5280)
    time = distance*3600/c
    print('Trip #{}: {:.2f} {:.2f}'.format(cnt, distance, time))
    cnt += 1