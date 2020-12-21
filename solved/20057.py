Dy = (0, 1, 0, -1)
Dx = (-1, 0, 1, 0)
def spread(y, x, D):
    global answer
    total = board[y][x]

    left, right = (D-1)%4, (D+1)%4
    dy, dx = Dy[D], Dx[D]
    left_dy, left_dx = Dy[left], Dx[left]
    right_dy, right_dx = Dy[right], Dx[right]

    arr = ((2*dy, 2*dx, 5), (left_dy+dy, left_dx+dx, 10), (right_dy+dy, right_dx+dx, 10), 
    (2*left_dy, 2*left_dx, 2), (2*right_dy, 2*right_dx, 2), (left_dy, left_dx, 7), 
    (right_dy, right_dx, 7), (left_dy-dy, left_dx-dx, 1), (right_dy-dy, right_dx-dx, 1) )

    save = total
    for ddy, ddx, percent in arr:
        ny, nx = y+ddy, x+ddx
        value = int(total*percent*0.01)
        save -= value
        if 0 <= ny < N and 0 <= nx < N:
            board[ny][nx] += value
        else:
            answer += value

    if 0 <= y + dy < N and 0 <= x + dx < N:
        board[y+dy][x+dx] += save
    else:
        answer += save


def move_straight(distance, y, x, direct):
    dy, dx = Dy[direct], Dx[direct]

    while distance:

        y, x = y+dy, x+dx
        spread(y, x, direct)
        board[y][x] = 0
        distance -= 1

    return y, x


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0

now_y, now_x = N//2, N//2
d = 0
for n in range(1, N):
    now_y, now_x = move_straight(n, now_y, now_x, d)
    d = (d+1)%4
    now_y, now_x = move_straight(n, now_y, now_x, d)
    d = (d+1)%4
now_y, now_x = move_straight(N-1, now_y, now_x, d)
print(answer)