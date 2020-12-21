N = int(input())
words = input()

total = 0
for i in range(len(words)):
    w = words[i]
    val = ord(w)-96
    total += val * 31**i
    total %= 1234567891
print(total)