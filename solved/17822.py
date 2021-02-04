from collections import deque

def rotate(num, direct, cnt):
    for n in range(num-1, row, num):
        for _ in range(cnt):
            if not direct:
                board[n].appendleft(board[n].pop())
            else:
                board[n].append(board[n].popleft())

def eraseNum():
    flag = False
    visited = [[False]*col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            if board[r][c]:
                visited[r][c] = True
                stack = [[r, c]]
                q = deque([[r, c]])

                while q:
                    y, x = q.popleft()

                    for dy, dx in ((-1 ,0), (0, 1), (1, 0), (0, -1)):
                        newY, newX = y+dy, (x+dx)%col
                        if not 0 <= newY < row: continue

                        if not visited[newY][newX] and board[newY][newX] == board[r][c]:
                            visited[newY][newX] = True
                            q.append([newY, newX])
                            stack.append([newY, newX])
                if len(stack) >= 2:
                    flag = True
                    while stack:
                        y, x = stack.pop()
                        board[y][x] = 0
    return flag


def calc():
    total, cnt = 0, 0
    for i in range(row):
        for j in range(col):
            if board[i][j]: 
                total += board[i][j]
                cnt += 1
    if not cnt: return

    avg = total/cnt
    for i in range(row):
        for j in range(col):
            if board[i][j]:
                if avg > board[i][j]:
                    board[i][j] += 1
                elif avg < board[i][j]:
                    board[i][j] -= 1

row, col, T = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(row)]

for _ in range(T):
    X, D, K = map(int, input().split()) # X배수 원판, 방향(시계 반시계), 회전수
    rotate(X, D, K)
    res = eraseNum()
    if not res:
        calc()

print(sum(map(sum, board)))