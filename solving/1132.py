from collections import defaultdict, deque
N = int(input())
words = [input() for _ in range(N)]

dic = defaultdict(int)
non_zero = set()
for word in words:
    l = len(word)
    non_zero.add(word[0])
    for i in range(l):
        char = word[i]
        dic[char] += 10**(l-i-1)

arr = sorted(dic.items(), key=lambda x:(x[1], x[0]), reverse=True)
if len(arr) >= 9 and arr[-1][0] in non_zero:
    tmp = deque()
    while arr and arr[-1][0] in non_zero:
        tmp.appendleft(arr.pop())
    if arr:
        tmp.append(arr.pop())
    arr.extend(tmp)

result = 0
num = 9
for key, value in arr:
    result += value * num
    num -= 1
print(result)