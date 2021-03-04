def rotate(block, diff):
    newBlock = [[0]*3 for _ in range(3)]
    if diff == 1:
        for r in range(3):
            for c in range(3):
                newBlock[c][2-r] = board[block][r][c]
    else:
        for r in range(3):
            for c in range(3):
                newBlock[2-c][r] = board[block][r][c]
    return newBlock

def init():
    dic = dict()
    dic['F'] = ['U2', 'R3', 'D0', 'L1']
    dic['B'] = ['U0', 'L3', 'D2', 'R1']
    dic['U'] = ['B0', 'R0', 'F0', 'L0']
    dic['D'] = ['F2', 'R2', 'B2', 'L2']
    dic['R'] = ['U1', 'B3', 'D1', 'F1']
    dic['L'] = ['U3', 'F3', 'D3', 'B1']

    tmp = {'F': 'r', 'B': 'o', 'U': 'w', 'D': 'y', 'R': 'b', 'L': 'g'}
    boarder = dict()
    for k, v in tmp.items():
        boarder[k] = [[v]*3 for _ in range(3)]

    return dic, boarder


dy = [
    [0, 0, 0],
    [0, 1, 2],
    [2, 2, 2],
    [2, 1, 0]
]

dx = [
    [0, 1, 2],
    [2, 2, 2],
    [2, 1, 0],
    [0, 0, 0]
]


for _ in range(int(input())):

    dice, board = init()
    N = int(input())
    orders = input().split()

    for order in orders:
        val, d = order[0], order[1]
        if d == '-':
            board[val] = rotate(val, -1)

            li = dice[val]
            for i in range(3):
                nowD, nowDirect = li[i][0], int(li[i][1])
                newD, newDirect = li[i+1][0], int(li[i+1][1])

                for j in range(3):
                    nowDy, nowDx = dy[nowDirect][j], dx[nowDirect][j]
                    newDy, newDx = dy[newDirect][j], dx[newDirect][j]  
                    board[nowD][nowDy][nowDx], board[newD][newDy][newDx] =\
                        board[newD][newDy][newDx], board[nowD][nowDy][nowDx]
        else:
            board[val] = rotate(val, 1)
            li = dice[val]
            for i in range(3, 0, -1):
                nowD, nowDirect = li[i][0], int(li[i][1])
                newD, newDirect = li[i-1][0], int(li[i-1][1])

                for j in range(3):
                    nowDy, nowDx = dy[nowDirect][j], dx[nowDirect][j]
                    newDy, newDx = dy[newDirect][j], dx[newDirect][j]  
                    board[nowD][nowDy][nowDx], board[newD][newDy][newDx] =\
                        board[newD][newDy][newDx], board[nowD][nowDy][nowDx]

    for b in board['U']:
        print(''.join(b))