N, S, D = map(int, input().split())
flag = False
for _ in range(N):
    s, d = map(int, input().split())
    if S > s and D < d: flag = True

print('Yes' if flag else 'No')