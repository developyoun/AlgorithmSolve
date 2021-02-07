V, T, S, D = map(int, input().split())

result = D/V
print('No' if T <= result <= S else 'Yes')