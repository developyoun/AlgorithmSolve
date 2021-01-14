def solve(value, depth):
    global result_max, result_min

    if depth == N:
        result_max = max(result_max, value)
        result_min = min(result_min, value)
        return

    if opers[0]: 
        opers[0] -= 1
        solve(value + numbers[depth], depth+1)
        opers[0] += 1
    if opers[1]: 
        opers[1] -= 1
        solve(value - numbers[depth], depth+1)
        opers[1] += 1
    if opers[2]: 
        opers[2] -= 1
        solve(value * numbers[depth], depth+1)
        opers[2] += 1
    if opers[3]: 
        opers[3] -= 1
        solve(int(value / numbers[depth]), depth+1)
        opers[3] += 1


N = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))


result_max, result_min = -float('INF'), float('INF')
solve(numbers[0], 1)
print(result_max)
print(result_min)