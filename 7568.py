N = int(input())

info = [list(map(int, input().split())) for _ in range(N)]
answer = []
for i in range(N):
    now_tall, now_weight = info[i]
    rank = 1
    for j in range(N):
        if i == j: continue
        new_tall, new_weight = info[j]
        if new_tall > now_tall and new_weight > now_weight: rank += 1
    answer.append(rank)
print(*answer)