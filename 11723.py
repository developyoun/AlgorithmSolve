import sys
input = sys.stdin.readline

s = set()

for _ in range(int(input())):
    word = input().split()
    if len(word) > 1:
        word, num = word[0], int(word[1])
    else:
        word = word[0]

    if word == 'add':
        s.add(num)
    elif word == 'check':
        if num in s:
            print(1)
        else:
            print(0)
    elif word == 'remove':
        s.discard(num)
    elif word == 'toggle':
        if num in s:
            s.discard(num)
        else:
            s.add(num)
    elif word == 'all':
        s = {i for i in range(1, 21)}
    elif word == 'empty':
        s = set()
    