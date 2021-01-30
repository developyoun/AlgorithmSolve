from itertools import combinations
from collections import deque


def spread(arr, cnt):
    visited = [[0]*N for _ in range(N)]
    q = deque()

    for y, x in arr:
        visited[y][x] = 1
        q.append([y, x])

    time = 0
    while q:
        if not cnt:
            return time

        for __ in range(len(q)):
            y, x = q.popleft()
            for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                newY, newX = y+dy, x+dx
                if 0 <= newY < N and 0 <= newX < N and not visited[newY][newX] and board[newY][newX] != 1:
                    visited[newY][newX] = visited[y][x]+1
                    q.append([newY, newX])
                    if not board[newY][newX]: cnt -= 1
        time += 1

    return -1


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

total = 0
virus = []
for i in range(N):
    for j in range(N):
        if not board[i][j]:
            total += 1
        if board[i][j] == 2:
            virus.append([i, j])

answer = float('INF')
for comb in combinations(virus, M):
    res = spread(comb, total)
    if res != -1:
        answer = min(answer, res)

print(-1 if answer == float('INF') else answer)
