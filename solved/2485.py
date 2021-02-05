def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

tmp = list()
for i in range(N-1):
    tmp.append(arr[i+1] - arr[i])

res = tmp[0]
for i in range(1, len(tmp)):
    res = gcd(res, tmp[i])
result = 0
for t in tmp:
    result += t//res - 1
print(result)