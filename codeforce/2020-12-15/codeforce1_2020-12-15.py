for _ in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    answers = [0] * N

    right, left = N-1, 0
    idx = 0
    while idx < N:
        
        if not idx & 1:
            answers[idx] = numbers[left]
            left += 1
        else:
            answers[idx] = numbers[right]
            right -= 1

        idx += 1
        
    print(*answers)