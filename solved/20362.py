import sys
from collections import defaultdict
input = sys.stdin.readline

N, answer_name = input().split()
answer = ''
dic = defaultdict(list)

arr = [input().split() for _ in range(int(N))]
for name, word in arr:
    if answer_name == name: 
        answer = word
        break
    dic[word].append(name)

print(len(dic[answer]))