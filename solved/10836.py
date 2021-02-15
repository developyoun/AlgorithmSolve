import sys  
input = sys.stdin.readline

def addBoard(arr):
    r, c = N-1, 0
    for a in arr:
        if r: board[r][c] += a; r -= 1
        else: board[r][c] += a; c += 1

def fillBug():
    for r in range(1, N):
        for c in range(1, N):
            board[r][c] = max(board[r-1][c], board[r][c-1], board[r-1][c-1])

N, M = map(int, input().split())
board = [[1]*N for _ in range(N)]

saved = [0] * (2*N-1)
for _ in range(M):
    a, b, c = map(int, input().split())
    for i in range(a, a+b):
        saved[i] += 1
    for i in range(a+b, a+b+c):
        saved[i] += 2

addBoard(saved)
fillBug()
for k in board:
    print(*k)