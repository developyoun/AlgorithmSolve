N = int(input())
info = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    info[a].append(b)
    info[b].append(a)

parents = [0] * (N+1)
parents[1] = 1
q = [1]
while q:
    now_node= q.pop()

    for new_node in info[now_node]:
        if not parents[new_node]:
            parents[new_node] = now_node
            q.append(new_node)

print('\n'.join(map(str, parents[2:])))