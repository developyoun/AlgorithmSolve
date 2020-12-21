def counting(target):
    result = 0
    for t in target:
        if int(t) & 1: result += 1
    return result

def solve(num, val):
    global MIN, MAX

    if len(num) == 1:
        if int(num) & 1: val += 1
        MIN = min(val, MIN)
        MAX = max(val, MAX)
        return
    
    elif len(num) == 2:
        res = counting(num)
        solve(str(int(num[0])+int(num[1])), val+res)

    else:
        for i in range(1, len(num)-1):
            for j in range(i+1, len(num)):
                res = counting(num)
                new_num = int(num[:i]) + int(num[i:j]) + int(num[j:])
                solve(str(new_num), res+val) 

N = input()
MIN, MAX = float('INF'), -1

cnt = 0
solve(N, 0)
print(MIN, MAX)