string1 = list(map(int, list(input())))
string2 = list(map(int, list(input())))

string3 = [0] * len(string2) + string1 + [0] * len(string2)
result = len(string1) + len(string2)

for i in range(len(string2)+len(string1)+1):
    cnt = 0
    new = string3[:]
    for j in range(len(string2)):
        value = string3[i+j] + string2[j]
        new[i+j] += string2[j]
        if value == 4: break
        else: cnt += 1
    else:
        zero = new.count(0)
        result = min(len(string3)-zero, result)
print(result)