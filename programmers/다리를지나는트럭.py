from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    arr = deque([0]*bridge_length)
    total = 0
    for truck in truck_weights:

        if total + truck <= weight:
            total += truck - arr.popleft()
            arr.append(truck)
            answer += 1
        else:
            while total+truck > weight:
                total -= arr.popleft()
                arr.append(0)
                answer += 1
            total += truck
            arr[-1] = truck
    while total:
        total -= arr.popleft()
        answer += 1

    return answer

print(solution(2, 10, [7,4,5,6]))