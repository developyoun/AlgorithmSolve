N = int(input())
arr = list(map(int, input().split()))
answer = []
sorted_arr = sorted(list(set(arr)), reverse=True)

cnt = 0
dic = {}
while sorted_arr:
    num = sorted_arr.pop()
    dic[num] = cnt
    cnt += 1

for a in arr:
    answer.append(dic[a])
print(*answer)