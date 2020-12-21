from collections import defaultdict

dic = defaultdict(int)
for _ in range(int(input())):
    name, extensions = input().split('.')
    dic[extensions] += 1

for s in sorted(dic.keys()):
    print(s, dic[s])