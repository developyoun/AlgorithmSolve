A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

print(min(A*P, B + ((P - C) * D if P > C else 0)))
