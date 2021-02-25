from collections import deque

def jump():
    visited = [[False]*col for _ in range(row)]
    visited[sy-1][sx-1] = True
    queue = deque()
    queue.append([sy-1, sx-1])

    while queue:
        y, x = queue.popleft()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < row and 0 <= newX < col and not visited[newY][newX]:
                if [newY, newX] == [ey-1, ex-1]: return True
                
                if board[newY][newX] == '0':
                    visited[newY][newX] = True
                    queue.append([newY, newX])
                else:
                    visited[newY][newX] = True
                    board[newY][newX] = '0'
    return False

row, col = map(int, input().split())
sy, sx, ey, ex = map(int, input().split())
board = [list(input()) for _ in range(row)]

cnt = 0
while True:
    cnt +=1
    if jump(): break
print(cnt)