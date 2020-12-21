numbers = list(map(int, input().split()))
flag = 0
for i in range(1, 9):
    if numbers[i-1] != i:
        break
else:
    flag = 1

for i in range(8):
    if numbers[i] != 8-i:
        break
else:
    flag = 2
dic = {0:'mixed', 1:'ascending', 2:'descending'}
print(dic[flag])