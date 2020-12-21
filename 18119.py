import sys
input = sys.stdin.readline

# char = set([chr(97+i) for i in range(26)])
answer = []
N, M = map(int, input().split())
words = [0] * N
for i in range(N):
    ww = input().rstrip()
    for w in ww:
        words[i] |= (1 << (ord(w)-97))


char = (1 << 26) - 1
for _ in range(M):
    o, x = input().split()

    bits = 1 << (ord(x) - 97)
    if o == '1':
        # if bits & char :
        char -= bits
    else:
        char |= bits
    
    cnt = 0
    for word in words:
        if word & char == word: 
            cnt += 1
    answer.append(cnt)
    
print('\n'.join(map(str, answer)))