def gcd(a, b)
    while b:
        a, b = b, a%b
    return a

N, s = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

arr = [abs(s-numbers[0])]
for i in range(N-1):
    arr.append(abs(numbers[i+1]-numbers[i]))

while len(arr) > 1:
    arr.append(gcd(arr.pop(), arr.pop()))
print(arr.pop())