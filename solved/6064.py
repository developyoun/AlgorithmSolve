import sys
input = sys.stdin.readline

for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    answer = -1
    x -= 1; y -= 1

    for i in range(x, M*N+1, M):
        if i % N == y:
            answer = i+1
            break
    print(answer)