for _ in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*(N+1) for _ in range(2)]
    dp[0][1] = board[0][0]
    dp[1][1] = board[1][0]

    for x in range(2, N+1):
        dp[0][x] = max(dp[0][x-1], dp[1][x-1] + board[0][x-1])
        dp[1][x] = max(dp[1][x-1], dp[0][x-1] + board[1][x-1])
    
    print(max(dp[0][-1], dp[1][-1]))