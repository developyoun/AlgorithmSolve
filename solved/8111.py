from collections import deque
def bfs(target):
    visited[1] = 1

    queue = deque()
    queue.append(1)
    while queue:
        now = queue.popleft()

        if not now % target:
            return True

        for val in (0, 1):
            new = (now*10+val)%target
            if visited[new] == -1:
                index[new] = now
                visited[new] = str(val)
                queue.append(new)
    return False

for _ in range(int(input())):
    N = int(input())
    index = [-1] * 200001
    visited = [-1] * 200001
    result = bfs(N)

    s = ''
    if result:
        idx = 0
        while idx != 1 and visited[idx] != -1:
            s += visited[idx]
            idx = index[idx]
        s += '1'
        print(s[::-1])
    else:
        print('BRAK')