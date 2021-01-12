from itertools import combinations

def check_line(arr, length):

    for p in range(length):
        for t in range(p+1, length):
            if arr[p][0] == arr[t][0] and arr[t][1] - arr[p][1] == 1:
                return False
    return True


def solve():
    for i in range(col):
        x, y = i, 0
        while y < row:
            if board[y][x]:
                x += 1
            elif 0 < x and board[y][x-1]:
                x -= 1
            y += 1

        if x != i: 
            return False

    return True


col, N, row = map(int, input().split())
board = [[0]*col for _ in range(row)]
for _ in range(N):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

queue = []
for i in range(row):
    for j in range(col-1):
        if not board[i][j]:
            if 0 < j and not board[i][j-1] and not board[i][j+1]:
                queue.append([i, j])
            elif j == 0 and not board[i][j+1]:
                queue.append([i, j])

flag = -1
for n in range(min(len(queue)+1, 4)):
    for k in combinations(queue, n):
        if not check_line(k, n): continue

        for r, c in k:
            board[r][c] = 1

        if solve(): 
            flag = n
            break

        for r, c in k:
            board[r][c] = 0

    if flag != -1:
        break

print(flag)