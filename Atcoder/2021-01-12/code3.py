N = int(input())
strings = set([input() for _ in range(N)])

s = set()
for string in strings:
    now = string
    if string[0] == '!':
        now = string[1:]
    
    if now in s:
        print(now)
        break
    s.add(now)

else:
    print('satisfiable')