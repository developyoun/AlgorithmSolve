# 남 동 북 서
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs(Y, X, num):
    visited[Y][X] = num
    q, cnt = [[Y, X]], 1
    
    while q:
        y, x = q.pop()

        for d in range(4):
            if board[y][x][d] == '0':
                newY, newX = y+dy[d], x+dx[d]
                if not visited[newY][newX]:
                    visited[newY][newX] = num
                    q.append([newY, newX])
                    cnt += 1
    return cnt


col, row = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

for i in range(row):
    for j in range(col):
        binary = bin(board[i][j])[2:]
        board[i][j] = '0'*(4-len(binary)) + binary

dic = {}
visited = [[0]*col for _ in range(row)]
number, max_result, room_cnt = 1, 0, 0
for i in range(row):
    for j in range(col):
        if not visited[i][j]:
            res = bfs(i, j, number)
            max_result = max(res, max_result)
            dic[number] = res
            room_cnt += 1
            number += 1

broke_max = max_result
for i in range(row):
    for j in range(col):
        for d in range(4):
            if board[i][j][d] == '1':
                newY, newX = i+dy[d], j+dx[d]
                if 0 <= newY < row and 0 <= newX < col and visited[i][j] != visited[newY][newX]:
                    num1, num2 = dic[visited[i][j]], dic[visited[newY][newX]]
                    broke_max = max(broke_max, num1+num2)
print(room_cnt)
print(max_result)
print(broke_max)