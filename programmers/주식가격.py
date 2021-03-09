def solution(prices):
    l = len(prices)
    answer = [0] * l

    stack = []
    for i in range(l):
        if not stack or stack[-1][0] <= prices[i]:
            stack.append([prices[i], i])
        else:
            while stack and stack[-1][0] > prices[i]:
                __, idx = stack.pop()
                answer[idx] = i - idx
            stack.append([prices[i], i])
    while stack:
        __, idx = stack.pop()
        answer[idx] = (l-1-idx)

    return answer