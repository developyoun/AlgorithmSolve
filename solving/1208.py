def dfs(start, end, value, flag):
    global result

    if start == end:
        if not flag:    # left
            try:
                dic[value] += 1
            except:
                dic[value] = 1
        else:   # right
            try:
                result += dic[S-value]
            except:
                pass
        return

    dfs(start+1, end, value, flag)
    dfs(start+1, end, value + arr[start], flag)

N, S = map(int, input().split())
arr = list(map(int, input().split()))

dic = {}
result = 0
leftStart, rightStart = 0, N//2

dfs(leftStart, rightStart, 0, 0)
dfs(rightStart, N, 0, 1)

if not S:
    result -= 1
print(result)