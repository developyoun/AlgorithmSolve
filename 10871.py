N, x = map(int, input().split())
answer = ''
for n in list(map(int, input().split())):
    if n < x:
        answer += str(n) + ' '
print(answer[:-1])