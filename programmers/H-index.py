def solution(citations):
    answer = 0
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            answer = l-i
            break
    return answer


# 20 19 18 1 ==> 3
solution([20, 19, 18, 1])