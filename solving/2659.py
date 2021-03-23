from collections import deque

arr = list(input().split())
li = []
save = []
for _ in range(4):
    li.append(''.join(arr))
    arr.append(arr.pop(0))
target = min(li)

flag = [0]*10000

def solve():
    cnt = 0
    for i in range(1111, 10000):
        string = str(i)
        if flag[i] or '0' in string:
            continue
        cnt += 1
        tmp = deque(string)
        for _ in range(4):
            num = int(''.join(tmp))
            flag[num] = cnt
            tmp.append(tmp.popleft())
    return -1

val = int(target)
result = solve()
print(flag[val])