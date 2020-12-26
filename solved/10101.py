a = int(input())
b = int(input())
c = int(input())

if a == b == c == 60:
    print("Equilateral")
elif a+b+c == 180 and len({a, b, c}) == 2:
    print("Isosceles")
elif a+b+c == 180 and len({a, b, c}) == 3:
    print("Scalene")
else:
    print("Error")