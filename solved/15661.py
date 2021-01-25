def calc(li):
    total, l = 0, len(li)
    for i in range(l):
        for j in range(i+1, l):
            a, b = li[i], li[j]
            total += board[a][b] + board[b][a]
    return total


from itertools import combinations
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

wholeArr = [i for i in range(N)]
whole = set(wholeArr)

result = float('INF')
for n in range(1, N//2+1):
    for A in combinations(wholeArr, n):
        B = list(whole - set(A))
        result = min(result, abs(calc(A)- calc(B)))
print(result)