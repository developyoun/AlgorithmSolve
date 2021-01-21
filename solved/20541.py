N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

dic = {}
A = sorted(A)
for i in range(N):
    if A[i] in dic: continue
    dic[A[i]] = i

result = []
for b in B:
    if b in dic:
        result.append(dic[b])
    else:
        result.append(-1)
        
print('\n'.join(map(str, result)))