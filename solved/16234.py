def allSum(data):
    result = 0
    for y, x in data:
        result += board[y][x]
    return result//len(data)


def checkCanSum():
    flag = False
    checked = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not checked[i][j]:
                checked[i][j] = True
                data = [[i, j]]
                q = [[i, j]]

                while q:
                    y, x = q.pop()

                    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                        newY, newX = y+dy, x+dx
                        if 0 <= newY < N and 0 <= newX < N and not checked[newY][newX]:
                            if L <= abs(board[y][x] - board[newY][newX]) <= R:
                                data.append([newY, newX])
                                q.append([newY, newX])
                                checked[newY][newX] = True

                if len(data) > 1:
                    flag = True
                    total = allSum(data)
                    while data:
                        y, x = data.pop()
                        board[y][x] = total
    return flag


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

time = 0
while checkCanSum():
    time += 1

print(time)
