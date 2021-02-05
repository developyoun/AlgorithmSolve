def isPrime(num):
    for k in range(2, int(num**0.5)+1):
        if not num % k: return False
    return True

for _ in range(int(input())):
    a, b = map(int, input().split())
    t = a + b

    flag = False
    for i in range(3, t//2+1, 2):
        if isPrime(i):
            if isPrime(t - i):
                flag = True
        if flag: break
    print('YES' if flag else 'NO')
