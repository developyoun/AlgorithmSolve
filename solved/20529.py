from collections import defaultdict

for _ in range(int(input())):
    N = int(input())
    dic = defaultdict(int)

    for val in input().split():
        dic[val] += 1
    
    arr1, arr2, arr3 = [], [], []
    result = float('INF')
    for key, val in dic.items():
        if val >= 3:
            result = 0; break
    if result:
        for key1, val1 in dic.items():
            if val1 == 2:
                for key2, val2 in dic.items():
                    if key1 == key2: continue
                    result = min(result, len(set(key1)-set(key2))*2)
            else:
                for key2, val2 in dic.items():
                    for key3, val3 in dic.items():
                        if key1 == key2 or key2 == key3 or key1 == key3: continue
                        result = min(result, len(set(key1)-set(key2))+len(set(key2)-set(key3))+len(set(key1)-set(key3)))
        print(result)
    else:
        print(0)