N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def solve(depth, result):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for a in arr:
        solve(depth+1, result + [a])
        
solve(0, [])