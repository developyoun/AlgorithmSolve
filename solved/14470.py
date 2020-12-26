arr = [int(input()) for _ in range(5)]

time = 0
if arr[0] < 0:
    time -= arr[0]*arr[2]
    arr[0] = 0
if not arr[0]:
    time += arr[3]
time += (arr[1]-arr[0])*arr[4]
print(time)