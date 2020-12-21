p = [0]*101
p[:10] = [1,1,1,2,2,3,4,5,7,9]

for i in range(10, 101):
    p[i] = p[i-1] + p[i-5]

for _ in range(int(input())):
    N = int(input())

    print(p[N-1])