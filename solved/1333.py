N, L, D = map(int, input().split())

d, l = 0, L
while N:
    N -= 1
    
    while d < l:
        d += D
    if l <= d < l+5:
        break
    l += 5+L

print(d)
