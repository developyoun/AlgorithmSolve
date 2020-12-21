def solve(div, y, x):
    
    if div == 1:
        answer[board[y][x]] += 1
        return

    check_one, check_zero = False, False
    for r in range(y, y+div):
        for c in range(x, x+div):
            if board[r][c]: check_one = True
            else: check_zero = True
    
    if check_one == check_zero == True:
        new_div = div//2
        for Y, X in ((y, x), (y, x+new_div), (y+new_div, x), (y+new_div, x+new_div)):
            solve(new_div, Y, X)
    else:
        answer[board[y][x]] += 1

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]
solve(N, 0, 0)
print(answer[0])
print(answer[1])