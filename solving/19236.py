dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

result = 0
def moveShark(weight, y, x, d, matrix, arr):
    global result
    result = max(result, weight)

    matrix, arr = moveFish(matrix, arr, y, x)

    for k in range(1, 4):
        newY, newX = y+dy[d]*k, x+dx[d]*k
        if 0 <= newY < 4 and 0 <= newX < 4 and matrix[newY][newX]:
            nxt, matrix[newY][newX] = matrix[newY][newX], 0
            __, __, newD = arr[nxt]
            arr[nxt] = [-1, -1, -1]

            moveShark(weight+nxt, newY, newX, newD, matrix, arr)

            arr[nxt] = [newY, newX, newD]
            matrix[newY][newX] = nxt
            

def moveFish(matrix, arr, warnY, warnX):
    newMatrix = [[matrix[i][j] for j in range(4)] for i in range(4)]
    newArr = [0] + [[Y, X, D] for Y, X, D in arr[1:]]

    for now in range(1, 17):
        if newArr[now] == [-1, -1, -1]: continue
        y, x, d = newArr[now]
        for k in range(8):
            newY, newX = y+dy[(d+k)%8], x+dx[(d+k)%8]
            
            if 0 <= newY < 4 and 0 <= newX < 4 and [newY, newX] != [warnY, warnX]:
                new = newMatrix[newY][newX]
                newMatrix[newY][newX], newMatrix[y][x] = newMatrix[y][x], newMatrix[newY][newX]
                newArr[now][0], newArr[now][1] = newY, newX
                if new:
                    newArr[new][0], newArr[new][1] = y, x
                newArr[now][2] = (d+k)%8
                break
    return newMatrix, newArr


board = [[] for _ in range(4)]
info = [0]*17
for i in range(4):
    li = list(map(int, input().split()))
    for j in range(0, 8, 2):
        num, direct = li[j], li[j+1]
        board[i].append(num)
        info[num] = [i, j//2, direct-1]

initWeight, board[0][0] = board[0][0], 0
__, __, initD = info[initWeight]
info[initWeight] = [-1, -1, -1]

moveShark(initWeight, 0, 0, initD, board, info)
print(result)