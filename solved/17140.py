row, col, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

time = 0

def sorting(matrix):
    r, c = min(100, len(matrix)), min(100, len(matrix[0]))

    newMatrix = []
    maxSize = 0
    if r >= c:
        for i in range(r):
            dic = {}
            for j in range(c):
                if not matrix[i][j]: continue
                try:
                    dic[matrix[i][j]] += 1
                except:
                    dic[matrix[i][j]] = 1
            
            saveValue, tmpArr = [], []
            for key, value in dic.items():
                saveValue.append([value, key])
            for v, k in sorted(saveValue):
                tmpArr.append(k)
                tmpArr.append(v)

            maxSize = max(maxSize, len(tmpArr))
            newMatrix.append(tmpArr)

        for li in newMatrix:
            li += [0]*(maxSize - len(li))

    else:
        for i in range(c):
            dic = {}
            for j in range(r):
                if not matrix[j][i]: continue
                try:
                    dic[matrix[j][i]] += 1
                except:
                    dic[matrix[j][i]] = 1
            
            saveValue, tmpArr = [], []
            for key, value in dic.items():
                saveValue.append([value, key])
            for v, k in sorted(saveValue):
                tmpArr.append(k)
                tmpArr.append(v)

            maxSize = max(maxSize, len(tmpArr))
            newMatrix.append(tmpArr)

        for li in newMatrix:
            li += [0]*(maxSize-len(li))

        newMatrix = rotate(newMatrix)
    return newMatrix


def rotate(newMatrix):
    r, c = len(newMatrix), len(newMatrix[0])
    result = [[0]*r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            result[j][i] = newMatrix[i][j]
    return result 

while time <= 100:
    if row <= len(board) and col <= len(board[0]) and board[row-1][col-1] == k: break
    board = sorting(board)
    time += 1

print(-1 if time > 100 else time)