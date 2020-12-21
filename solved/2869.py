a, b, v = map(int, input().split())

cnt = (v-a) // (a-b) + 1 + (1 if (v-a) % (a-b) else 0)
print(cnt)