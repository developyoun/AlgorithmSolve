t = int(input())
a, t = t//300, t%300
b, t = t//60, t%60
c, t = t//10, t%10

if not t:
    print(a, b, c)
else:
    print(-1)