from itertools import permutations


def solve(p):
    order = p[:3] + [0] + p[3:]
    idx = 0

    tmp = 0
    for n in range(N):
        one = two = three = out = 0

        while out < 3:
            number = order[idx]
            point = board[n][number]

            if not point:
                out += 1
            elif point == 1:
                tmp += three
                three, two, one = two, one, 1
            elif point == 2:
                tmp += two + three
                three, two, one = one, 1, 0
            elif point == 3:
                tmp += one + two + three
                three, two, one = 1, 0, 0
            else:
                tmp += one + two + three + 1
                three, two, one = 0, 0, 0

            idx = (idx+1) % 9
    # print(tmp)
    return tmp


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = 0
arr = [1, 2, 3, 4, 5, 6, 7, 8]
for perm in permutations(arr, 8):
    res = solve(list(perm))
    result = max(result, res)
print(result)
