import sys
input = sys.stdin.readline
N, M = map(int, input().split())
dic = {}
for _ in range(N):
    a, b = input().split()
    dic[a] = b

answer = []
for _ in range(M):
    word = input().rstrip()
    answer.append(dic[word])
print('\n'.join(answer))