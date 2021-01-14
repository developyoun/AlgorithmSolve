def solve(y, x, value, depth):
    
    if depth == 6:
        s.add(value)
        return

    for dy, dx in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        new_y, new_x = y+dy, x+dx
        if 0 <= new_y < 5 and 0 <= new_x < 5:
            solve(new_y, new_x, value*10+board[new_y][new_x], depth+1)


board = [list(map(int, input().split())) for _ in range(5)]
s = set()

for i in range(5):
    for j in range(5):
        solve(i, j, board[i][j], 1)

print(len(s))