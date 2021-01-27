from collections import defaultdict, deque

def solve(s, Y, X):
    saveDict = defaultdict(int)
    saveDict[s] = 1

    q = deque()
    q.append(s)

    while q:
        string = q.popleft()

        if string == '123456780':
            return saveDict[string]-1

        idx = string.index('0')
        y, x = idx//3, idx%3

        string2list = list(string)
        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if 0 <= y+dy < 3 and 0 <= x+dx < 3:
                d = dy*3 + dx
                string2list[idx], string2list[idx+d] = string2list[idx+d], string2list[idx]
                newString = ''.join(string2list)
                if not saveDict[newString]:
                    saveDict[newString] = saveDict[string] + 1
                    q.append(newString)
                string2list[idx], string2list[idx+d] = string2list[idx+d], string2list[idx]
    # print(saveDict)
    return -1

board = [list(map(int, input().split())) for _ in range(3)]

string = ''
for li in board:
    for s in li:
        string += str(s)

initY, initX = -1, -1
for i in range(9):
    if string[i] == '0':
        initY, initX = i//3, i%3
        break

value = solve(string, initY, initX)
print(value)