def dfs(idx, saved):
    global result

    if idx == K:
        cnt = 0
        for li in arr:
            if not li - saved: cnt +=1 
        result = max(result, cnt)
        return

    dfs(idx+1, saved | {people[idx][0]})
    dfs(idx+1, saved | {people[idx][1]})

N, M = map(int, input().split())
arr = [set(map(int, input().split())) for _ in range(M)]
K = int(input())
people = [list(map(int, input().split())) for _ in range(K)]

result = 0
dfs(0, set())
print(result)