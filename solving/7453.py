import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a); B.append(b); C.append(c), D.append(d)

AB = defaultdict(int)
for a in A:
    for b in B:
        AB[a+b] += 1
        
result = 0
for c in C:
    for d in D:
        try:
            result += AB[-(c+d)]
        except:
            pass
        
print(result)
