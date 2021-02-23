def check(y1, x1, y2, x2):
    if abs(y1-y2) == 2 and abs(x1-x2) == 1:
        return True
    elif abs(y1-y2) == 1 and abs(x1-x2) == 2:
        return True
    return False

order = []
for _ in range(36):
    order.append(input())

dic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6}

cnt = 0
if order[0][0] not in dic: cnt = -100
sy, sx, ey, ex = dic[order[0][0]], int(order[0][1]), dic[order[35][0]], int(order[35][1])
y, x = sy, sx
save = [[y, x]]
if 0 < y <= 6 and 0 < x <= 6:
    cnt += 1
    for val in order[1:]:
        if val[0] not in dic: break
        r, c = dic[val[0]], int(val[1])

        if not (0 < r <= 6 and 0 < c <= 6): break
        if not check(y, x, r, c): break
        if [r, c] in save: break
        save.append([r, c])
        y, x = r, c 
        cnt += 1

print('Invalid' if cnt!=36 or not check(sy, sx, ey, ex) else 'Valid')