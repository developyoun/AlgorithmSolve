for _ in range(int(input())):
    N = int(input())
    
    dp = [0] * (1000000+1)
    dp[1], dp[2], dp[3] = 1, 2, 4
    div = 1000000009

    for i in range(4, N+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % div

    print(dp[N])