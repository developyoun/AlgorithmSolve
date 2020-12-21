def get_distance(a, b, c, d):
    return abs(a-c) + abs(b-d)

for _ in range(int(input())):
    N = int(input())
    pos = [list(map(int, input().split())) for _ in range(N+2)]
    visited = [[float('INF')] * (N+2) for _ in range(N+2)]

    for i in range(N+2):
        for j in range(N+2):
            if i == j: continue
            if get_distance(pos[i][0], pos[i][1], pos[j][0], pos[j][1]) <= 1000:
                visited[i][j] = 1
    
    for k in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                visited[i][j] = min(visited[i][j], visited[i][k] + visited[k][j])
    # print(visited)
    print('sad' if visited[0][-1] == float('INF') else 'happy')