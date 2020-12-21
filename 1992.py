def solve(div, y, x):
    global answer

    if div == 1:
        answer += board[y][x]
        return

    check_one, check_zero = False, False
    for r in range(y, y+div):
        for c in range(x, x+div):
            if board[r][c] == '1': check_one = True
            elif board[r][c] == '0': check_zero = True
    
    if check_zero == check_one == True:
        new_div = div//2
        answer += '('
        for new_y, new_x in ((y, x), (y, x+new_div), (y+new_div, x), (y+new_div, x+new_div)):
            solve(new_div, new_y, new_x)
        answer += ')'

    elif check_zero:
        answer += '0'
    elif check_one:
        answer += '1'

N = int(input())
board = [input() for _ in range(N)]
answer = ''
solve(N, 0, 0)
print(answer)