board = [list(map(int, input().split())) for _ in range(2)]

arr = [([0,0], [1,0], [0,1], [1,1]), ([1,0], [1,1], [0,0], [0,1]), 
    ([1,1], [0,1], [1,0], [0,1]),([0,1], [0,0], [1,1], [1,0])]

value = -float('INF')
result = -1
for i in range(4):
    a, b, c, d = arr[i]
    tmp = board[a[0]][a[1]]/board[b[0]][b[1]] + board[c[0]][c[1]]/board[d[0]][d[1]]
    if value < tmp:
        value = tmp
        result = i
print(result)