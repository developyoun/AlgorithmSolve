while True:
    col, row = map(int, input().split())
    if [row, col] == [0, 0]: break
    board = [list(map(int, input().split())) for _ in range(row)]

    result = 0
    for r in range(row):
        for c in range(col):
            if board[r][c]:
                result += 1
                board[r][c] = 0

                q = [[r, c]]
                while q:
                    y, x = q.pop()

                    for dy in (-1, -1, 0, 1, 1, 1, 0, -1):
                        for dx in (0, 1, 1, 1, 0, -1, -1, -1):
                            new_y, new_x = y+dy, x+dx
                            if 0 <= new_y < row and 0 <= new_x < col and board[new_y][new_x]:
                                board[new_y][new_x] = 0
                                q.append([new_y, new_x])

    print(result)