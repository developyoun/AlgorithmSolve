N = int(input())
arr = list(map(int, input().split()))

s = set()
for a in arr:
    tmp = set()
    for n in s:
        tmp.add(a+n)

    s |= tmp
    s.add(a)

whole = set([i for i in range(1, sum(arr)+2)])
print(min(whole - s))