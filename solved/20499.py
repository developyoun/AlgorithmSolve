a, b, c = map(int, input().split('/'))

if not b or a+c < b:
    print('hasu')
else:
    print('gosu')