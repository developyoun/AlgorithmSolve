for _ in range(int(input())):
    dic = {}
    for _ in range(int(input())):
        a, b = input().split()
        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1
    
    result = 1
    for k, v in dic.items():
        result *= v+1
    print(result - 1) 
