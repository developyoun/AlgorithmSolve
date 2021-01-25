N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

target = list(map(int, input().split()))
start = target[0]
flag, idx = False, 1

stack = [start]
while idx < N:
    if stack:
        if target[idx] in arr[stack[-1]]:
            stack.append(target[idx])
            idx += 1
        else:
            stack.pop()
    else:
        break

print(1 if idx == N and start == 1 else 0)