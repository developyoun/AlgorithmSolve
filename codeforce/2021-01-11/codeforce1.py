for _ in range(int(input())):
    N = int(input())
    red = input()
    blue = input()

    r, b = 0, 0
    for i in range(N):
        if red[i] > blue[i]:
            r += 1
        elif red[i] < blue[i]:
            b += 1
    
    if r > b: print('RED')
    elif r < b: print('BLUE')
    else: print('EQUAL')