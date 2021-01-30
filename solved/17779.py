def calculate(arr, i, j, left, right):
    global result
    p1, p2, p3, p4 = 0, 0, 0, 0
    for y in range(i+left):
        for x in range(j+1):
            if arr[y][x]: break
            p1 += board[y][x]
    
    for y in range(i+right+1):
        for x in range(N-1, j, -1):
            if arr[y][x]: break
            p2 += board[y][x]
    
    for y in range(i+left, N):
        for x in range(j-left+right):
            if arr[y][x]: break
            p3 += board[y][x]
    
    for y in range(i+right+1, N):
        for x in range(N-1, j-left+right-1, -1):
            if arr[y][x]: break
            p4 += board[y][x]
    p5 = total - (p1+p2+p3+p4)
    MAX, MIN = max(p1, p2, p3, p4 ,p5), min(p1, p2, p3, p4, p5)
    result = min(result, MAX-MIN)    

def mark(y, x, left, right):
    marking = [[0]*N for _ in range(N)]
    marking[y][x] = 1
    for ll in range(1, left+1):
        for rr in range(1, right+1):
            marking[y+ll][x-ll] = marking[y+rr][x+rr] = marking[y+ll+rr][x-ll+rr] = marking[y+ll+rr][x+rr-ll] = 1
    calculate(marking, y, x, left, right)

def getPoint(y, x):
    for left in range(1,N):
        for right in range(1, N):
            if 0 <= y+left+right < N and 0 <= x-left < x+right < N:
                mark(y, x, left, right)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

total = 0
for r in range(N):
    for c in range(N):
        total += board[r][c]

result = float('INF')
for r in range(N-2):
    for c in range(1, N-1):
        getPoint(r, c)

print(result)