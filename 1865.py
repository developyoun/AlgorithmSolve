import sys
input = sys.stdin.readline
inf = sys.maxsize

def solve():
    visited = [inf] * (N+1)
    for _ in range(N):
        for now_node in range(1, N+1):
            for new_node, distance in board[now_node]:
                if visited[new_node] > distance + visited[now_node]:
                    visited[new_node] = distance + visited[now_node]
    
    for now_node in range(1, N+1):
        for new_node, distance in board[now_node]:
            if visited[new_node] > distance + visited[now_node]:
                return True
    return False


for _ in range(int(input())):
    N, M, W = map(int, input().split())
    board = [[] for _ in range(N+1)]

    for _ in range(M):
        i, j, k = map(int, input().split())
        board[i].append([j, k])
        board[j].append([i, k])
    for _ in range(W):
        i, j, k = map(int, input().split())
        board[i].append([j, -k])

    flag = solve()
    print('YES' if flag else 'NO')