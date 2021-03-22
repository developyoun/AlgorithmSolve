while True:
    N = int(input())
    if N == -1: break

    board = [list(input()) for _ in range(N)]
    dp = [[0]*N for _ in range(N)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            if board[i][j] != '0' and dp[i][j]:
                dis = int(board[i][j])
                if i+dis < N:
                    dp[i+dis][j] += dp[i][j]
                if j+dis < N:
                    dp[i][j+dis] += dp[i][j]

    print(dp[N-1][N-1])