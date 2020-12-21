goal = int(input())
can_input = input()

numbers = set([str(i) for i in range(10)])
if can_input != '0':
    numbers -= set(input().split())

answer = abs(100-goal)

for n in range(10**6):
    str2n = str(n)
    if not set(str2n) - numbers:
        answer = min(answer, abs(int(str2n)-goal)+len(str2n)) 
print(answer)