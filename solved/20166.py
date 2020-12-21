from collections import defaultdict

def solve(y, x, word):

    if 5 == len(word):
        return
        
    for dy, dx in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
        new_y, new_x = (y+dy)%row, (x+dx)%col
        new_word = word + board[new_y][new_x]
        dic[new_word] += 1
        solve(new_y, new_x, new_word)


row, col, k = map(int, input().split())
board = [input() for _ in range(row)]

dic = defaultdict(int)
for r in range(row):
    for c in range(col):
        dic[board[r][c]] += 1
        solve(r, c, board[r][c])

for _ in range(k):
    target = input()
    print(dic[target])