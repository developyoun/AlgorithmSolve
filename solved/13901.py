direct = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

row, col = map(int, input().split())
board = [[0]*col for _ in range(row)]

for _ in range(int(input())):
    r, c = map(int, input().split())
    board[r][c] = 1

y, x = map(int, input().split())
directions = list(map(int, input().split()))
board[y][x] = 1
d = 0

while True:

    for i in range(4):
        nd = (directions[(d+i)%4]-1)
        new_y, new_x = y+direct[nd][0], x+direct[nd][1]
        if 0 <= new_y < row and 0 <= new_x < col and not board[new_y][new_x]:
            d = d+i
            break
    else:
        break
    board[new_y][new_x] = 1
    y, x = new_y, new_x

print(y, x)
