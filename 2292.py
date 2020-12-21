target = int(input())

now, cnt = 1, 1
while True:
    if now >= target: break
    now += cnt*6
    cnt += 1
print(cnt)