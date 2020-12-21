from collections import deque
import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    now, target = map(int, input().split())
    visited = ['']*10000
    visited[now] = 'A'
    queue = deque([now])
    
    while queue:
        number = queue.popleft()

        if visited[target]: break

        arr = {}
        arr['D'] = (number*2) % 10000
        arr['S'] = number-1 if number else 9999
        arr['L'] = (number%1000) * 10 + number//1000
        arr['R'] = (number//10) + 1000 * (number%10)

        for key, value in arr.items():
            if not visited[value]:
                visited[value] = visited[number] + key
                queue.append(value)
        
    answer.append(visited[target][1:])
print('\n'.join(answer))