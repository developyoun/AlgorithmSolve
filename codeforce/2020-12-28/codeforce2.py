for _ in range(int(input())):
    R = int(input())
    reds = list(map(int, input().split()))
    B = int(input())
    blues = list(map(int, input().split()))

    max_red, total_red = 0, 0
    for r in reds:
        total_red += r
        max_red = max(max_red, total_red)

    max_blue, total_blue = 0, 0
    for b in blues:
        total_blue += b
        max_blue = max(max_blue, total_blue)
    
    print(max_red + max_blue)