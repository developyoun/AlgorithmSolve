def check(num):
    if num == 1: return False
    elif num == 2: return True
    elif not num%2: return False

    for k in range(3, int(num**0.5)+1, 2):
        if not num % k: return False
    return True

start, end = map(int, input().split())
answer = []
for i in range(start, end+1):
    if check(i): answer.append(i)
print('\n'.join(map(str, answer)))

