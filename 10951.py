while True:
    try:
        tmp = input()
        a, b = map(int, tmp.split())
        print(a+b)
    except:
        break