from collections import deque
dic = {'1':'3', '2':'4', '3':'1', '4':'2'}

N = int(input())
arr = input().split()
target = ''.join(arr)
rev = ''.join([dic[a] for a in arr[::-1]])
M = int(input())

tmp = []
for _ in range(M):
    tmp.append(deque(input().split()))
answer = []
for m in range(M):
    now = deque(a for a in tmp[m])

    for _ in range(N):
        s = ''.join(now)
        if s == target or s == rev:
            answer.append(tmp[m])
            break
        now.append(now.popleft())
print(len(answer))
for a in answer:
    print(*a)