def distance(y1, x1, y2, x2):
    return abs(y1-y2) + abs(x1-x2)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = float('INF')
for r1 in range(1, N-1):
    for c1 in range(1, N-1):

        for r2 in range(1, N-1):
            for c2 in range(1, N-1):
                if distance(r1, c1, r2, c2) > 2:

                    for r3 in range(1, N-1):
                        for c3 in range(1, N-1):
                            if distance(r1, c1, r3, c3) > 2 and distance(r2, c2, r3, c3) > 2:

                                total = board[r1][c1] + board[r2][c2] + board[r3][c3]
                                for r, c in ((r1, c1), (r2, c2), (r3, c3)):
                                    for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                                        total += board[r+dy][c+dx]
                                result = min(result, total)
print(result)