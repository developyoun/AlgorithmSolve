a1, p1 = map(int, input().split())
a2, p2 = map(int, input().split())

b1 = a1*p2
b2 = a2*a2*3.14159265359*p1

print('Whole pizza' if b1 < b2 else 'Slice of pizza')