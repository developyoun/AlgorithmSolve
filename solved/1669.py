now, target = map(int, input().split())

val = target - now
if val:
    tmp = int(val**0.5)
    answer = tmp*2-1 + (val-tmp**2)//tmp + (1 if (val-tmp**2)%tmp else 0)
else:
    answer = 0
print(answer)