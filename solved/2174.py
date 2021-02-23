dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dic = {'N':0, 'E':1, 'S':2, 'W':3}

col, row = map(int, input().split())

board = [[0]*(col+1) for _ in range(row+1)]
info = dict()

N, M = map(int, input().split())
for n in range(N):
    c, r, direct = input().split()
    r, c = row-int(r)+1, int(c)
    board[r][c] = n+1
    info[n+1] = [r, c, dic[direct]]

result = ''
for m in range(M):
    robot, order, cnt = input().split()
    robot, cnt = int(robot), int(cnt)
    if result: continue

    if order == 'L':
        info[robot][2] = (info[robot][2]-cnt)%4
    elif order == 'R':
        info[robot][2] = (info[robot][2]+cnt)%4
    else:
        y, x, d = info[robot]
        for _ in range(cnt):
            newY, newX = y+dy[d], x+dx[d]
            if not 0 < newY <= row or not 0 < newX <= col:
                result = 'Robot {} crashes into the wall'.format(robot)
                break
            elif board[newY][newX]:
                result = 'Robot {} crashes into robot {}'.format(robot, board[newY][newX])
                break
            else:
                board[y][x], board[newY][newX] = 0, robot
                y, x = newY, newX
        info[robot] = [y, x, d]
if result:
    print(result)
else:
    print('OK')