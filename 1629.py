a, b, c = map(int, input().split())
int2bin = bin(b)[2:][::-1]

answer = 1
prev = a
for i in range(len(int2bin)):
    if int2bin[i] == '1':
        answer = (prev*answer) % c
    prev = (prev * prev) % c

print(answer)
