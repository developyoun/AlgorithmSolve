for _ in range(int(input())):
    answer = 0
    start, end = map(int, input().split())

    diff = end - start
    if diff:
        sqrt = int(diff**0.5)
        double = sqrt**2
        answer = sqrt*2 - 1 + (diff-double) // sqrt + (1 if (diff-double)%sqrt else 0)
    
    print(answer)