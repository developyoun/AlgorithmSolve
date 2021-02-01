def calc(num):
    res = N/num - (n-1)/2
    if res == int(res):
        return True
    return False

N = int(input())

result = 2
for n in range(2, int(N**0.5)+1):
    if calc(n): 
        result += 2
print(result)