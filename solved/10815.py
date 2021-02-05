N = int(input())
now = {i: True for i in list(map(int, input().split()))}

M = int(input())
result = []
for num in list(map(int, input().split())):
    try:
        if now[num]: result.append(1)
    except:
        result.append(0)
print(*result)