import sys
input = sys.stdin.readline
N = int(input())
S = int(input())
string = input().rstrip()

target = 'I' + 'OI'*N
answer = 0

tmp = 0
idx = 1
while idx < S-1:
    if string[idx-1:idx+2] == 'IOI':
        tmp += 1
        if tmp == N:
            answer += 1
            tmp -= 1
        idx += 1
    else:
        tmp = 0
    idx += 1
print(answer)