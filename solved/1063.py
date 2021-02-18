dic = {'R':[0, 1], 'L':[0, -1], 'B':[1, 0], 'T':[-1, 0], 
    'RT':[-1, 1], 'LT':[-1, -1], 'RB':[1, 1], 'LB':[1, -1]}
word = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}

k, s, N = input().split()
king = [8-int(k[1]), word[k[0]]]
stone = [8-int(s[1]), word[s[0]]]

for _ in range(int(N)):
    order = input()
    dy, dx = dic[order]
    
    newY, newX = king[0]+dy, king[1]+dx
    if not (0 <= newY < 8 and 0 <= newX < 8): continue

    if [newY, newX] == stone:
        ny, nx = stone[0]+dy, stone[1]+dx
        if not (0 <= ny < 8 and 0 <= nx < 8): continue
        else:
            stone[0], stone[1] = ny, nx
            king[0], king[1] = newY, newX
    else:
        king[0], king[1] = newY, newX

print(chr(king[1]+65)+str(8-king[0]))
print(chr(stone[1]+65)+str(8-stone[0]))