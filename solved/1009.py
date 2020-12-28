dic = {0:[1], 1:[6,2,4,8], 2:[1,3,9,7], 3:[6,4], 
    4:[5], 5:[6], 6:[1,7,9,3], 7:[6,8,4,2], 8:[1, 9], 9:[10]}

for _ in range(int(input())):
    a, b = map(int, input().split())

    a = (a-1)%10
    c = b % len(dic[a])
    print(dic[a][c])