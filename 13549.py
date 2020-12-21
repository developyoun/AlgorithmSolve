from collections import deque
inf = float('INF')
pos, goal = map(int, input().split())

def solve():
    answer = abs(goal - pos)
    
    if pos >= goal:
        return answer

    visited = [inf] * 100001
    visited[pos] = 0
    dq = deque([pos])
    while dq:
        now = dq.popleft()

        if now == goal:
            answer = visited[now]
            break

        if now*2 <= 10**5:
            new = now*2
            if visited[new] == inf:
                dq.appendleft(new)
                visited[new] = visited[now]

        else:
            answer = min(answer, abs(goal - now*2)+visited[now])
        
        for new in (now-1, now+1):
            if 0 > new: 
                continue
            elif new > 10**5: 
                answer = min(answer, abs(goal-new)+visited[now] + 1)
            else:
                if visited[new] == inf:
                    dq.append(new)
                    visited[new] = visited[now] + 1
    return answer

print(solve())