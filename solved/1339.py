from collections import defaultdict
N = int(input())
dic = defaultdict(int)

for _ in range(N):
    string = input()
    num = 0
    for i in range(len(string)-1, -1, -1):
        s = string[i]
        dic[s] += 10**num
        num += 1

num, result = 9, 0
for val in sorted(dic.values(), reverse=True):
    result += num*val
    num -= 1
print(result)