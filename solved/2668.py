def dfs(num, s):
    global answer
    if num in s:
        if i == num:
            answer |= s
        return

    s.add(num)
    dfs(numbers[num], s)


N = int(input())
numbers = [0] + [int(input()) for _ in range(N)]
visited = [False] * (N+1)

answer = set()
for i in range(1, N+1):
    if i in answer: continue
    dfs(numbers[i], {i})
print(len(answer))
print('\n'.join(map(str, sorted(answer))))