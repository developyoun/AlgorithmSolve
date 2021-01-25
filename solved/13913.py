from collections import deque

def solve():
    time = 0

    while queue:
        for _ in range(len(queue)):
            nowNode = queue.popleft()

            if nowNode == E:
                return time

            for newNode in (nowNode-1, nowNode+1, nowNode*2):
                if 0 <= newNode < 200001 and visited[newNode] == -1:
                    visited[newNode] = nowNode
                    queue.append(newNode)
        time += 1


S, E = map(int, input().split())

visited = [-1] * 200001
visited[S] = 0
queue = deque()
queue.append(S)

result = solve()
resultArr = [E]
while resultArr[-1] != S:
    resultArr.append(visited[resultArr[-1]])
print(result)
print(*resultArr[::-1])