arr = [int(input()) for _ in range(6)]
print(sum(sorted(arr[:4])[-3:]) + max(arr[4:]))