col, row = map(int, input().split())
sx, sy = map(int, input().split())
time = int(input())

r, c = time%(row*2), time%(col*2)

dy = 1
while r:
    if sy == row:
        dy = -1
    if sy == 0:
        dy = 1
    sy += dy
    r -= 1

dx = 1
while c:
    if sx == col:
        dx = -1
    if sx == 0:
        dx = 1
    sx += dx
    c -=1

print(sx, sy)