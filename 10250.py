for _ in range(int(input())):
    h, w, n = map(int, input().split())
    
    if not n % h:
        f = h
        b = n//h
    else:
        f = n % h
        b = n // h+1

    print(str(f) + ('0'+str(b) if len(str(b)) == 1 else str(b)))