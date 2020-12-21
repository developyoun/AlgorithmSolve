n, k = map(int, input().split())
numbers = list([str(i) for i in range(1, n+1)])

answer = []
idx = k-1
while numbers:
    answer.append(numbers[idx])
    numbers.remove(numbers[idx])
    idx += k-1
    if numbers:
        idx %= len(numbers)
print('<'+', '.join(answer)+'>')
