def multiple(arr1, arr2):

    result = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            value = 0
            for i in range(N):
                value += (arr1[r][i] * arr2[i][c]) % 1000
            result[r][c] = value % 1000
    return result


N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
answer = [[0]*N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if y == x: answer[y][x] = 1


int2bin = bin(K)[2:][::-1]
for b in int2bin:
    if b == '1':
        answer = multiple(answer, matrix)
    matrix = multiple(matrix, matrix)


for a in answer:
    print(*a)