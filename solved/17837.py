dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def move():
    tmpArr = []
    for number in range(K):
        y, x, d = info[number]
        newY, newX = y+dy[d], x+dx[d]

        if not (0 <= newY < N and 0 <= newX < N) or board[newY][newX] == 2: #파란색 or 벽
            newD = (d+2)%4
            info[number][2] = newD
            newY, newX = y+dy[newD], x+dx[newD]

        if not (0 <= newY < N and 0 <= newX < N) or board[newY][newX] == 2:
            continue

        if not board[newY][newX]:  #흰색
            while table[y][x]:
                last = table[y][x].pop()
                tmpArr.append(last)
                if last == number: break

            while tmpArr:
                now = tmpArr.pop()
                info[now][0], info[now][1] = newY, newX
                table[newY][newX].append(now)
            

        else:   #빨간색
            while table[y][x]:
                last = table[y][x].pop()
                info[last][0], info[last][1] = newY, newX
                table[newY][newX].append(last)
                if last == number: break
        
        r, c, __ = info[number]

        if len(table[r][c]) >= 4: 
            return True
        
    return False


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
table = [[[] for _ in range(N)] for _ in range(N)]

dic = {1:1, 2:3, 3:0, 4:2}
info = []
for k in range(K):
    R, C, D = map(int, input().split())
    table[R-1][C-1].append(k)
    info.append([R-1, C-1, dic[D]])

time = 1
while time <= 1000:
    if move(): break
    
    time += 1

print(time if time <= 1000 else -1)