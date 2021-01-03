# 목장 건설하기
row, col = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(row)]

"""
input:
6 6
0 0 0 1 0 0
0 0 0 2 1 0
0 0 2 0 0 0
0 1 0 0 0 0
2 0 0 0 0 0
0 0 0 0 0 0
"""

dp = [[0]*(col+1) for _ in range(row+1)]

for i in range(1,row+1):
    for j in range(1, col+1):
        if not board[i-1][j-1]:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

print(max(map(max, dp)))