def subSmell():
    for i in range(N):
        for j in range(N):
            if smellMap[i][j][1]:
                smellMap[i][j][1] -= 1


def moveShark(cnt):

    stack = []
    for n in range(1, M+1):
        if sharkInfo[n]:
            y, x, d = sharkInfo[n]
            board[y][x] = 0
            for i in range(4):
                dy, dx = dic[directInfo[n][d][i]]
                new_y, new_x = y+dy, x+dx
                if 0 <= new_y < N and 0 <= new_x < N and not smellMap[new_y][new_x][1]:
                    stack.append([n, new_y, new_x, directInfo[n][d][i]])
                    break
            else:
                for i in range(4):
                    dy, dx = dic[directInfo[n][d][i]]
                    new_y, new_x = y+dy, x+dx
                    if 0 <= new_y < N and 0 <= new_x < N and smellMap[new_y][new_x][0] == n:
                        stack.append([n, new_y, new_x, directInfo[n][d][i]])
                        break
    
    subSmell()
    while stack:
        number, y, x, d = stack.pop()
        if board[y][x]:
            cnt -= 1
            if board[y][x] < number:
                sharkInfo[number] = 0
            else:
                other, board[y][x] = board[y][x], number
                sharkInfo[number] = [y, x, d]
                sharkInfo[other] = 0
                smellMap[y][x] = [number, K]
        else:
            sharkInfo[number] = [y, x, d]
            board[y][x] = number
            smellMap[y][x] = [number, K]
    return cnt


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
smellMap = [[[0, 0] for _ in range(N)] for _ in range(N)]

tmp = list(map(int, input().split()))
sharkInfo = [0]*(M+1)
for i in range(N):
    for j in range(N):
        if board[i][j]:
            num = board[i][j]
            smellMap[i][j] = [num, K] 
            sharkInfo[num] = [i, j, tmp[num-1]]

directInfo = dict()
for m in range(1, M+1):
    savedict = dict()
    for mm in range(1, 5):
        savedict[mm] = list(map(int, input().split()))
    directInfo[m] = savedict

dic = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}
reverse = {1: 2, 2: 1, 3: 4, 4: 3}

cnt = M
for time in range(1, 1001+1):
    cnt = moveShark(cnt)
    if cnt <= 1:
        break

print(time if time != 1001 else -1)
