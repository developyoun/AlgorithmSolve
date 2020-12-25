a = list(int(input()) for _ in range(4))

s1 = sorted(a)
s2 = sorted(a, reverse=True)
s3 = set(a)

if len(s3) == 1:
    print('Fish At Constant Depth')
elif s1 == a and len(s3) == 4:
    print('Fish Rising')
elif s2 == a and len(s3) == 4:
    print('Fish Diving')
else:
    print('No Fish')