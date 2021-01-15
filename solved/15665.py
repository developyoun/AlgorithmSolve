def solve(depth, result):
    
    if depth == M:
        print(*result)
        return
    
    for a in arr:
        solve(depth+1, result + [a])

answer = set()
N, M = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

solve(0, [])