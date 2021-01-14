def check_attack(y, x, n):
    for i in range(y, y+n):
        for j in range(x, x+n):
            if not board[i][j]: return False
    return True

def attach(y, x, n):
    for i in range(y, y+n):
        for j in range(x, x+n):
            board[i][j] = 0

def detach(y, x, n):
    for i in range(y, y+n):
        for j in range(x, x+n):
            board[i][j] = 1

def solve(i, j, whole, cnt):
    global result

    if cnt >= result:
        return
    
    if not whole:
        result = cnt
        return

    for y in range(i, 10):
        if y == i+1: j = 0
        for x in range(j, 10):
            if not board[y][x]: continue
            for n in range(5, 0, -1):
                if y+n > 10 or x+n > 10: continue 
                if not check_attack(y, x, n) or not rest[n]: continue

                rest[n] -= 1; attach(y, x, n)
                solve(y, x+n, whole - n**2, cnt+1)
                rest[n] += 1; detach(y, x, n)
            return

board = [list(map(int, input().split())) for _ in range(10)]
rest = [0, 5, 5, 5, 5, 5]

total = 0
for r in range(10):
    for c in range(10):
        if board[r][c]: total += 1


result = 26
solve(0, 0, total, 0)
print(result if result < 26 else -1)