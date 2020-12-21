from collections import defaultdict

row, col, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]
MAX = max(map(max, board))
MIN = min(map(min, board))

answer_time, answer_height = float('INF'), 0

dic = defaultdict(int)
for i in range(row):
    for j in range(col):
        dic[board[i][j]] += 1

while MIN <= MAX:

    time, rest, needs = 0, 0, 0
    for key, val in dic.items():
        
        if key > MAX:
            res = val * (key - MAX)
            time += 2 * res
            rest += res
        elif key < MAX:
            res = val * (MAX - key)
            time += res
            needs += res
    if b >= needs - rest:
        if answer_time > time:
            answer_time = time
            answer_height = MAX
    MAX -= 1
print(answer_time, answer_height)