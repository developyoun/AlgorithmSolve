from collections import deque
import sys
input = sys.stdin.readline

def init():
    global result
    for i in (0, row-1):
        for j in range(col):
            if 'a' <= board[i][j] <= 'z':
                char = board[i][j].upper()
                if not keys[char]: keys[char] = True
                board[i][j] = '.'
            if board[i][j] == '$':
                board[i][j] = '.'
                result += 1
                
    for j in (0, col-1):
        for i in range(1, row-1):
            if 'a' <= board[i][j] <= 'z':
                char = board[i][j].upper()
                if not keys[char]: keys[char] = True
                board[i][j] = '.'
            if board[i][j] == '$':
                board[i][j] = '.'
                result += 1


def getEntrance(arr):
    entrance = deque()
    for i in (0, row-1):
        for j in range(col):
            if board[i][j] == '.' or ('A' <= board[i][j] <= 'Z' and keys[board[i][j]]):
                entrance.append([i, j])
                arr[i][j] = True
                
    for j in (0, col-1):
        for i in range(1, row-1):
            if board[i][j] == '.' or ('A' <= board[i][j] <= 'Z' and keys[board[i][j]]):
                entrance.append([i, j])
                arr[i][j] = True

    return entrance

def searchKey():
    visited = [[False]*col for _ in range(row)]
    queue = getEntrance(visited)

    getKey = False
    cnt = 0
    while queue:
        y, x = queue.popleft()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY < row and 0 <= newX < col and not visited[newY][newX] and board[newY][newX] != '*':
                if board[newY][newX] == '.':
                    visited[newY][newX] = True
                    queue.append([newY, newX])

                elif board[newY][newX] == '$':
                    visited[newY][newX] = True
                    board[newY][newX] = '.'
                    queue.append([newY, newX])
                    cnt += 1

                else:
                    if 'A' <= board[newY][newX] <= 'Z' and keys[board[newY][newX]]:
                        visited[newY][newX] = True
                        queue.append([newY, newX])
                    elif 'a' <= board[newY][newX] <= 'z':
                        char = board[newY][newX].upper()
                        if not keys[char]: 
                            keys[char] = True
                            getKey = True
                        board[newY][newX] = '.'
                        visited[newY][newX] = True
                        queue.append([newY, newX])
    return getKey, cnt

for _ in range(int(input())):
    keys = {chr(ord('A')+i):False for i in range(26)}
    row, col = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(row)]

    for s in input():
        if s == '0': break
        keys[s.upper()] = True

    result = 0
    init()

    while True:
        flag, num = searchKey()
        result += num
        if not flag: break
    
    print(result)