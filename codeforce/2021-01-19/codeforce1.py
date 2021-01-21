import sys
input = sys.stdin.readline

dic = {'1':'0', '0':'1'}
result = []
for _ in range(int(input())):
    N = int(input())
    bits = list(input())
    answer = '1'

    prev = '1'
    for n in range(1, N):
        if prev != bits[n-1]:
            answer += bits[n]
            prev = bits[n]
        else:
            if bits[n-1] == bits[n]:
                answer += dic[bits[n]]
                prev = dic[bits[n]]
            else:
                answer += '1'
                prev = '1'
    result.append(answer)

print('\n'.join(result))