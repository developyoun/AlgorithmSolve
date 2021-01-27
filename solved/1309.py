N = int(input())
board = [[0, 0, 0] for _ in range(N)]
board[0][:] = [1, 1, 1]

for i in range(1, N):
    board[i][0] = (board[i-1][0] + board[i-1][1] + board[i-1][2]) % 9901
    board[i][1] = (board[i-1][0] + board[i-1][2]) % 9901
    board[i][2] = (board[i-1][0] + board[i-1][1]) % 9901

print(sum(board[N-1]) % 9901)