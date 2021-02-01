from heapq import heappush, heappop

N = int(input())
number = []
for _ in range(N):
    heappush(number, int(input()))

total = 0
while len(number) >= 2:
    num1, num2 = heappop(number), heappop(number)
    total += num1 + num2
    heappush(number, num1+num2)

print(total)