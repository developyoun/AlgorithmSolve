from itertools import combinations

def solve(arr):
    visited = [[False]*5 for _ in range(5)]
    while arr:
        y, x = arr.pop()
        visited[y][x] = 1

    q = [[y, x]]
    visited[y][x] = 2
    cnt = 1
    while q:
        y, x = q.pop()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            newY, newX = y+dy, x+dx
            if 0 <= newY <5 and 0 <= newX < 5 and visited[newY][newX] == 1:
                visited[newY][newX] = 2
                q.append([newY, newX])
                cnt += 1
                
    return True if cnt == 7 else False

board = [input() for _ in range(5)]
result = 0
for comb in combinations(range(25), 7):
    arr = []
    cntY, cntS = 0, 0
    for num in comb:
        r, c = num//5, num%5
        arr.append([r, c])
        if board[r][c] == 'Y': cntY += 1
        else: cntS += 1
    if cntY > cntS: continue
    result += solve(arr)
print(result)