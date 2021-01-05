def boom(r, c, arr):
    saved = [[r, c]]

    queue = [[r, c]]
    while queue:
        y, x = queue.pop()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            new_y, new_x = y+dy, x+dx
            if 0 <= new_y < 12 and 0 <= new_x < 6:
                if board[new_y][new_x] == board[r][c] and not arr[new_y][new_x]:
                    arr[new_y][new_x] = True
                    queue.append([new_y, new_x])
                    saved.append([new_y, new_x])
    if len(saved) >= 4:
        while saved:
            y, x = saved.pop()
            board[y][x] = '.'
        return 1

    return 0


def check_bubble():

    result = 0
    checked = [[False]*6 for _ in range(12)]
    
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not checked[i][j]:
                checked[i][j] = True
                result += boom(i, j, checked)
    
    return result


def pull_down():
    for x in range(6):
        stack = []
        for y in range(12):
            if board[y][x] != '.':
                stack.append(board[y][x])
                board[y][x] = '.'
        idx = 11
        while stack:
            board[idx][x] = stack.pop()
            idx -= 1


board = [list(input()) for _ in range(12)]

answer = 0
while True:
    res = check_bubble()
    if not res: break
    answer += 1
    pull_down()

print(answer)
