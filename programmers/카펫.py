def solution(brown, yellow):
    answer = []

    B = (brown+4)//2

    for r in range(B-1, 0, -1):
        c = B - r
        if r * c == brown + yellow:
            answer = [r, c]
            break

    return answer