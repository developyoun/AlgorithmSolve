n = int(input())
num = n//2 + 1

if n & 1:
    print(2 * num * (num+1))
else:
    print(num**2)