a = int(input())
b = int(input())
c = b - a

text = 'You are speeding and your fine is $'
if c <= 0:
    print('Congratulations, you are within the speed limit!')
elif 1 <= c <= 20:
    print(text + '100.')
elif 21 <= c <= 30:
    print(text + '270.')
else:
    print(text + '500.')