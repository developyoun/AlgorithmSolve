string1 = list(map(int, list(input())))
string2 = list(map(int, list(input())))

result = len(string1) + len(string2)

for i in range(len(string1)):
    for j in range(len(string2), -1, -1):
        