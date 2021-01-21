N = int(input())
cards = [0] + list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, N+1):
        if 0 <= i + j <= N:
            cards[i+j] = max(cards[i+j], cards[i]+cards[j])
print(cards[N])