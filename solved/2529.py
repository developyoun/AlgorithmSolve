def solve(idx, arr):
    global MAX, MIN

    if idx == N:
        val = ''.join(map(str, arr))

        MIN = min(MIN, val)
        MAX = max(MAX, val)
        return

    for n in range(10):
        if used[n]: continue

        if oper[idx] == '<' and arr[-1] < n:
            used[n] = True
            solve(idx+1, arr + [n])
            used[n]= False

        elif oper[idx] == '>' and arr[-1] > n:
            used[n] = True
            solve(idx+1, arr + [n])
            used[n] = False


N = int(input())
oper = input().split()

used = [False] * 10
MAX, MIN = '0'*10, '9'*10

for i in range(10):
    used[i] = True
    solve(0, [i])
    used[i] = False

print(MAX+'\n'+MIN)