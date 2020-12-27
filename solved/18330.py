n = int(input())
k = int(input())

if n <= k+60:
    print(n*1500)
else:
    print((n-60)*3000 + (60-k)*1500)

