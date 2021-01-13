e, s, m = 0, 0, 0
E, S, M = map(int, input().split())

result = 1
while [e, s, m] != [E-1, S-1, M-1]:
    e, s, m = (e+1)%15, (s+1)%28, (m+1)%19
    result += 1
print(result)