from heapq import heappop, heappush
from collections import defaultdict

def solution(operations):
    answer = []
    values = defaultdict(int)
    MIN, MAX = [], []

    for oper in operations:
        order, num = oper.split()
        num = int(num)

        if order == 'I':
            values[num] += 1
            heappush(MIN, num)
            heappush(MAX, -num)

        else:
            if num == -1:
                while MIN and not values[MIN[0]]: heappop(MIN)
                if MIN:
                    target = heappop(MIN)
                    values[target] -= 1
            else:
                while MAX and not values[-MAX[0]]: heappop(MAX)
                if MAX:
                    target = heappop(MAX)
                    values[-target] -= 1

    while MIN and not values[MIN[0]]: heappop(MIN)
    while MAX and not values[-MAX[0]]: heappop(MAX)

    if MIN or MAX:
        answer = [-MAX[0], MIN[0]]
    else:
        answer = [0, 0]
    return answer