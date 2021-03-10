def solution(array, commands):
    answer = []

    for com in commands:
        i, j, k = com
        num = sorted(array[i-1:j])[k-1]
        answer.append(num)

    return answer