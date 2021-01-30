def spring():
    for i in range(N):
        for j in range(N):
            if info[i][j]:
                info[i][j].sort()
                last = 0
                for idx in range(len(info[i][j])):
                    age = info[i][j][idx]
                    if age <= board[i][j]:
                        board[i][j] -= age
                        info[i][j][idx] += 1
                    else:
                        last = len(info[i][j])-idx
                        break

                while last:
                    value = info[i][j].pop()
                    summer(i, j, value)
                    last -= 1

def summer(y, x, e):
    board[y][x] += e//2

def fall():
    for i in range(N):
        for j in range(N):
            for age in info[i][j]:
                if not age % 5:
                    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)):
                        newY, newX = i+dy, j+dx
                        if 0 <= newY < N and 0 <= newX < N:
                            info[newY][newX].append(1)

def winter():
    for i in range(N):
        for j in range(N):
            board[i][j] += energyMap[i][j]

N, M, K = map(int, input().split())
energyMap = [list(map(int, input().split())) for _ in range(N)]
board = [[5]*N for _ in range(N)]
info = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r, c, o = map(int, input().split())
    info[r-1][c-1].append(o)

for _ in range(K):
    spring()
    fall()
    winter()

result = 0
for r in info:
    for c in r:
        result += len(c)
print(result)