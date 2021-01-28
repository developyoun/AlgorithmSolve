arr = input()[:-1].split(', ')
base, first = arr[0].split()
strings = [first] + arr[1:]

for s in strings:
    for idx in range(len(s)-1, -1, -1):
        if s[idx].isalpha():
            words, last = s[:idx+1], ''
            for i in range(len(s)-1, idx, -1):
                if s[i] == '[': last += ']'
                elif s[i] == ']': last += '['
                else: last += s[i]
            print(base + last +' '+words+';')
            break