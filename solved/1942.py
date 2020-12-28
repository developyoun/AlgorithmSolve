for _ in range(3):
    start, end = input().split()
    sh, sm, ss = start.split(':')
    eh, em, es = end.split(':')

    start = int(sh+sm+ss)
    end = int(eh+em+es)

    cnt = 0
    while start != end:
        if not start % 3: cnt += 1

        start += 1
        h = start//10000
        m = (start-h*10000)//100
        s = start - h*10000 - m*100
        if s >= 60:
            s -= 60
            m += 1
        if m >= 60:
            m -= 60
            h += 1
        if h >= 24:
            h -= 24
        start = h*10000 + m*100 + s
        
    if not end % 3:
        cnt += 1
    print(cnt)