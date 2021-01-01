arr = [25, 10, 5, 1]

for _ in range(int(input())):
    k = int(input())
    result = [0, 0, 0, 0]
    for i in range(4):
        result[i] = k//arr[i]
        k = k%arr[i]
        
    print(*result)