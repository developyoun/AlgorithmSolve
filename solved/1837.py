P, K = map(int, input().split())
flag = [False] * K
flag[1] = True

for k in range(2, K):
    if not flag[k]:
        for m in range(k+k, K, k):
            flag[m] = True

result = 0
for k in range(2, K):
    if not P%k and not flag[k]:
        result = k
        break

print('BAD {}'.format(result) if result else 'GOOD')