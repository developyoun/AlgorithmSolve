N, M = map(int, input().split())
known = list(map(int, input().split()))[1:]
party = [list(map(int, input().split())) for _ in range(M)]

connect = [set() for _ in range(N+1)]
for p in party:
    S = set(p[1:])
    for n in p[1:]:
        connect[n] |= S

for n in range(1, N+1):
    for m in connect[n]:
        connect[m] |= connect[n]

answer = 0
total_set = set()
for k in known:
    total_set |= connect[k]
for p in party:
    target = set(p[1:])
    if not total_set & target:
        answer += 1
print(answer)