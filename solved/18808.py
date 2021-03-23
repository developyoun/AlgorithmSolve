def rotate(matrix, Y, X):
    C, R = Y, X
    tmp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            tmp[i][j] = matrix[Y-j-1][i]
    return tmp

def check_attach(idx):
    nowBlock = blocks[idx]
    
    for _ in range(4):
        Y, X = len(nowBlock), len(nowBlock[0])
        for i in range(row):
            for j in range(col):
                flag = True
                if i+Y <= row and j+X <= col:
                    for y in range(Y):
                        for x in range(X):
                            if board[i+y][j+x] + nowBlock[y][x] > 1:
                                flag = False
                    if flag: 
                        attach(i, j, nowBlock)
                        return 
        nowBlock = rotate(nowBlock, Y, X)
        
    return False, -1, -1


def attach(R, C, matrix):
    y, x = len(matrix), len(matrix[0])
    for i in range(y):
        for j in range(x):
            board[i+R][j+C] += matrix[i][j]
    

row, col, N = map(int, input().split())
board = [[0]*col for _ in range(row)]

blocks = []
for _ in range(N):
    r, c = map(int, input().split())
    block = [list(map(int, input().split())) for _ in range(r)]
    blocks.append(block)

for i in range(N):
    check_attach(i)
    
result = 0
for a in board:
    result += a.count(1)
print(result)