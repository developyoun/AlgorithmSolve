dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, 1, 1, 1, 0, -1, -1, -1)

def move_fireball():
    for n in range(len(info)):
        y, x, weight, speed, direct = info[n]
        info[n][0], info[n][1] = (y+dy[direct]*speed) % N, (x+dx[direct]*speed) % N

def sum_fireball():
    dic = dict()

    while info:
        y, x, weight, speed, direct = info.pop()
        if (y, x) in dic:
            dic[(y, x)].append([weight, speed, direct])
        else:
            dic[(y, x)] = [[weight, speed, direct]]

    for key, value in dic.items():
        if len(value) >= 2:
            total_weight, total_speed, direct_check = 0, 0, value[0][2] & 1
            flag = False
            for weight, speed, direct in value:
                if direct & 1 != direct_check: flag = True
                total_weight += weight
                total_speed += speed

            if total_weight >= 5:
                cur_weight = total_weight // 5
                cur_speed = total_speed // len(value)

                for cur_direct in ((1, 3, 5, 7) if flag else (0, 2, 4, 6)):
                    info.append([key[0], key[1], cur_weight, cur_speed, cur_direct])
        else:
            value = value[0]
            info.append([key[0], key[1], value[0], value[1], value[2]])



N, M, K = map(int, input().split())
info = []
for num in range(M):
    r, c, m, s, d = map(int, input().split())
    info.append([r-1, c-1, m, s, d])

for _ in range(K):
    move_fireball()
    sum_fireball()
result = 0

for __, __, value_weight, __, __ in info:
    result += value_weight
print(result)