row, col = map(int, input().split())
board = [input() for _ in range(row)]

answer = row*col
for i in range(row-7):
    for j in range(col-7): 
        res1 = 0
        for r in range(i, i+8):
            for c in range(j, j+8):
                if (r+c) & 1:
                    if board[r][c] == 'W': res1 += 1
                else:
                    if board[r][c] == 'B': res1 += 1


        res2 = 0
        for r in range(i, i+8):
            for c in range(j, j+8):
                if (r+c) & 1:
                    if board[r][c] == 'B': res2 += 1
                else:
                    if board[r][c] == 'W': res2 += 1
        
        answer = min(answer, res1, res2)
print(answer)