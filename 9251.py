import sys
input = sys.stdin.readline

sub1 = input().rstrip()
sub2 = input().rstrip()

dp = [[0]*(len(sub1)+1) for _ in range(len(sub2)+1)]

for i in range(1, len(sub2)+1):
    for j in range(1, len(sub1)+1):
        if sub2[i-1] == sub1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])