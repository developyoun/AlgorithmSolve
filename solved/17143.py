dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
reverse_direct = {0:1, 1:0, 2:3, 3:2}
dic = {}

def moveFish():

    queue = []
    for number, infos in dic.items():
        if infos:
            y, x, speed, dd, size = infos
            board[y][x] = 0

            for _ in range(speed):
                if not 0 <= y+dy[dd] < row or not 0 <= x+dx[dd] < col:
                    dd = reverse_direct[dd]
                y, x = y+dy[dd], x+dx[dd]
            queue.append([number, y, x, speed, dd, size])
    
    for num, y, x, speed, dd, size in queue:
        if board[y][x]:
            origin = board[y][x]
            if dic[origin][4] < size:
                board[y][x] = num
                dic[num] = [y, x, speed, dd, size]
                dic[origin] = 0
            else:
                dic[num] = 0
        else:
            board[y][x] = num
            dic[num] = [y, x, speed, dd, size]


def catching(c):
    value = 0
    for r in range(row):
        if board[r][c]:
            number = board[r][c]
            value += dic[number][4]
            dic[number] = 0
            board[r][c] = 0
            break 
    return value

row, col, M = map(int, input().split())
board = [[0]*col for _ in range(row)]
result = 0

for m in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = m
    dic[m] = [r-1, c-1, s, d-1, z]

for x in range(col):
    result += catching(x)
    moveFish()

print(result)